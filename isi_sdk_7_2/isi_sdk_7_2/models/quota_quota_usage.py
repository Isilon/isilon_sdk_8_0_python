# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class QuotaQuotaUsage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'inodes': 'int',
        'logical': 'int',
        'physical': 'int'
    }

    attribute_map = {
        'inodes': 'inodes',
        'logical': 'logical',
        'physical': 'physical'
    }

    def __init__(self, inodes=None, logical=None, physical=None):  # noqa: E501
        """QuotaQuotaUsage - a model defined in Swagger"""  # noqa: E501

        self._inodes = None
        self._logical = None
        self._physical = None
        self.discriminator = None

        self.inodes = inodes
        self.logical = logical
        self.physical = physical

    @property
    def inodes(self):
        """Gets the inodes of this QuotaQuotaUsage.  # noqa: E501

        Number of inodes (filesystem entities) used by governed data.  # noqa: E501

        :return: The inodes of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._inodes

    @inodes.setter
    def inodes(self, inodes):
        """Sets the inodes of this QuotaQuotaUsage.

        Number of inodes (filesystem entities) used by governed data.  # noqa: E501

        :param inodes: The inodes of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if inodes is None:
            raise ValueError("Invalid value for `inodes`, must not be `None`")  # noqa: E501

        self._inodes = inodes

    @property
    def logical(self):
        """Gets the logical of this QuotaQuotaUsage.  # noqa: E501

        Apparent bytes used by governed data.  # noqa: E501

        :return: The logical of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._logical

    @logical.setter
    def logical(self, logical):
        """Sets the logical of this QuotaQuotaUsage.

        Apparent bytes used by governed data.  # noqa: E501

        :param logical: The logical of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if logical is None:
            raise ValueError("Invalid value for `logical`, must not be `None`")  # noqa: E501

        self._logical = logical

    @property
    def physical(self):
        """Gets the physical of this QuotaQuotaUsage.  # noqa: E501

        Bytes used for governed data and filesystem overhead.  # noqa: E501

        :return: The physical of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._physical

    @physical.setter
    def physical(self, physical):
        """Sets the physical of this QuotaQuotaUsage.

        Bytes used for governed data and filesystem overhead.  # noqa: E501

        :param physical: The physical of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if physical is None:
            raise ValueError("Invalid value for `physical`, must not be `None`")  # noqa: E501

        self._physical = physical

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QuotaQuotaUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
