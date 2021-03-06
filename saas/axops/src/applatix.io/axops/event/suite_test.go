// Copyright 2015-2016 Applatix, Inc. All rights reserved.
package event_test

import (
	"applatix.io/axdb/axdbcl"
	"applatix.io/axdb/core"
	"applatix.io/axerror"
	"applatix.io/axops"
	"applatix.io/axops/event"
	"applatix.io/axops/user"
	"applatix.io/test"
	"encoding/json"
	"flag"
	"fmt"
	"github.com/Shopify/sarama"
	"gopkg.in/check.v1"
	"os/exec"
	"runtime/debug"
	"testing"
	"time"
)

const (
	axdburl        = "http://localhost:8080/v1"
	axopsurl       = "http://localhost:8085/v1"
	axopsexurl     = "http://localhost:8086/v1"
	gatewayurl     = "http://localhost:9090/v1"
	workflowadcurl = "http://localhost:9090/v1"
	axmonurl       = "http://localhost:9090/v1"
	axnotifierurl  = "http://localhost:9090/v1"
	fixmgrurl      = "http://localhost:9091/v1"
	kafkaurl       = "localhost:9092"
	schedulerurl   = "http://localhost:9090/v1"
	verbose        = true
)

// Use a client explicitly. Later replace the client with one that uses TLS
var axdbClient = axdbcl.NewAXDBClientWithTimeout(axdburl, time.Second*60)

//var axopsClient = restcl.NewRestClient(axopsurl)
//var axopsExternalClient = restcl.NewRestClient(axopsexurl)
var axkafkaClient sarama.SyncProducer = nil

type S struct{}

func Test(t *testing.T) { check.TestingT(t) }

var _ = check.Suite(&S{})

func startKafka(c *check.C) {
	//start up zookeeper first
	c.Logf("starting zookeeper")
	exec.Command("export KAFKA_HEAP_OPTS=-Xmx128M -Xms64M").Run()
	cmd := exec.Command("/usr/bin/zookeeper-server-start", "-daemon", "/etc/kafka/zookeeper.properties")
	err := cmd.Run()
	if err != nil {
		fail(c)
	}
	c.Logf("started zookeeper")

	// start up kafka server
	c.Logf("starting kafka")
	exec.Command("export KAFKA_HEAP_OPTS=-Xmx375M -Xms256M").Run()
	cmd = exec.Command("/usr/bin/kafka-server-start", "-daemon", "/etc/kafka/server.properties")
	err = cmd.Run()
	if err != nil {
		fail(c)
	}
	c.Logf("started kafka")
	time.Sleep(10 * time.Second)
}

func (s *S) SetUpSuite(c *check.C) {
	flag.Parse()

	// We test against our REST API. So we need to start our main program here.
	core.InitLoggers()
	core.InitDB(core.CassandraNodes)
	core.ReloadDBTable()
	go core.StartRouter(true)

	// wait for axdb server to be running
	for i := 0; i < 120; i++ {
		var bodyArray []interface{}
		err := axdbClient.Get("axdb", "status", nil, &bodyArray)
		if err == nil {
			break
		} else {
			fmt.Println(err)
		}
		time.Sleep(1 * time.Second)
	}

	startKafka(c)
	// startup axops server
	axops.InitTest(axdburl, gatewayurl, workflowadcurl, axmonurl, axnotifierurl, fixmgrurl, schedulerurl)

	event.Init("localhost:9092")
	//used for TestAsyncSequential
	event.InitConsumerGroup([]string{"localhost:9092"}, "TESTEvent", []string{"topic"}, 1)

	retryCount := 0
	for {
		retryCount++
		var err error
		axkafkaClient, err = sarama.NewSyncProducer([]string{kafkaurl}, nil)
		if err == nil {
			break
		} else {
			if retryCount < 300 {
				time.Sleep(1 * time.Second)
			} else {
				c.Logf("failed to create a kafka producer")
				fail(c)
			}
		}
	}

	axops.CreateTables()

	internalRouter := axops.GetRounter(true)
	go internalRouter.Run(":8085")

	externalRouter := axops.GetRounter(false)
	go externalRouter.Run(":8086")

	go test.StartFakeRouter(9090)
	go test.StartFixtureFakeRouter(9091)

	// simple wait for the server to start
	time.Sleep(2 * time.Second)

	user.InitGroups()
	user.InitAdminInternalUser()
}

func PostOneEvent(c *check.C, topic string, key string, op string, data interface{}) {
	valueStr, err := json.Marshal(packKafkaMessage(op, data))
	c.Assert(err, check.IsNil)

	produceMsg := &sarama.ProducerMessage{Topic: topic, Key: sarama.StringEncoder(key),
		Value: sarama.StringEncoder(valueStr)}

	p, o, err := axkafkaClient.SendMessage(produceMsg)
	fmt.Printf("partition=%d, offset=%d, msg=%v", p, o, produceMsg)
	if topic == "topic" {
		c.Logf("partition=%d, offset=%d, msg=%v", p, o, produceMsg)
	}

	c.Assert(err, check.IsNil)
}

func packKafkaMessage(op string, payload interface{}) interface{} {
	data := map[string]interface{}{
		"Op": op, "Payload": payload,
	}

	return data
}

func fail(c *check.C) {
	debug.PrintStack()
	c.FailNow()
}

func checkError(c *check.C, err *axerror.AXError) {
	c.Assert(err, check.IsNil)
}

type GeneralGetResult struct {
	Data []map[string]interface{} `json:"data,omitempty"`
}
