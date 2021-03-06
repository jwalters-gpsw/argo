# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ObjectReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, kind=None, namespace=None, name=None, uid=None, api_version=None, resource_version=None, field_path=None):
        """
        V1ObjectReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'namespace': 'str',
            'name': 'str',
            'uid': 'str',
            'api_version': 'str',
            'resource_version': 'str',
            'field_path': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'namespace': 'namespace',
            'name': 'name',
            'uid': 'uid',
            'api_version': 'apiVersion',
            'resource_version': 'resourceVersion',
            'field_path': 'fieldPath'
        }

        self._kind = kind
        self._namespace = namespace
        self._name = name
        self._uid = uid
        self._api_version = api_version
        self._resource_version = resource_version
        self._field_path = field_path

    @property
    def kind(self):
        """
        Gets the kind of this V1ObjectReference.
        Kind of the referent. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ObjectReference.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ObjectReference.
        Kind of the referent. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ObjectReference.
        :type: str
        """

        self._kind = kind

    @property
    def namespace(self):
        """
        Gets the namespace of this V1ObjectReference.
        Namespace of the referent. More info: http://kubernetes.io/docs/user-guide/namespaces

        :return: The namespace of this V1ObjectReference.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1ObjectReference.
        Namespace of the referent. More info: http://kubernetes.io/docs/user-guide/namespaces

        :param namespace: The namespace of this V1ObjectReference.
        :type: str
        """

        self._namespace = namespace

    @property
    def name(self):
        """
        Gets the name of this V1ObjectReference.
        Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :return: The name of this V1ObjectReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ObjectReference.
        Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :param name: The name of this V1ObjectReference.
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """
        Gets the uid of this V1ObjectReference.
        UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

        :return: The uid of this V1ObjectReference.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this V1ObjectReference.
        UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

        :param uid: The uid of this V1ObjectReference.
        :type: str
        """

        self._uid = uid

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ObjectReference.
        API version of the referent.

        :return: The api_version of this V1ObjectReference.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ObjectReference.
        API version of the referent.

        :param api_version: The api_version of this V1ObjectReference.
        :type: str
        """

        self._api_version = api_version

    @property
    def resource_version(self):
        """
        Gets the resource_version of this V1ObjectReference.
        Specific resourceVersion to which this reference is made, if any. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :return: The resource_version of this V1ObjectReference.
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """
        Sets the resource_version of this V1ObjectReference.
        Specific resourceVersion to which this reference is made, if any. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :param resource_version: The resource_version of this V1ObjectReference.
        :type: str
        """

        self._resource_version = resource_version

    @property
    def field_path(self):
        """
        Gets the field_path of this V1ObjectReference.
        If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: \"spec.containers{name}\" (where \"name\" refers to the name of the container that triggered the event) or if no container name is specified \"spec.containers[2]\" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.

        :return: The field_path of this V1ObjectReference.
        :rtype: str
        """
        return self._field_path

    @field_path.setter
    def field_path(self, field_path):
        """
        Sets the field_path of this V1ObjectReference.
        If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: \"spec.containers{name}\" (where \"name\" refers to the name of the container that triggered the event) or if no container name is specified \"spec.containers[2]\" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.

        :param field_path: The field_path of this V1ObjectReference.
        :type: str
        """

        self._field_path = field_path

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1ObjectReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
