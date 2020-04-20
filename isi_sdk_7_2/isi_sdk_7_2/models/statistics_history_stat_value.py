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


class StatisticsHistoryStatValue(object):
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
        'time': 'int',
        'value': 'str'
    }

    attribute_map = {
        'time': 'time',
        'value': 'value'
    }

    def __init__(self, time=None, value=None):  # noqa: E501
        """StatisticsHistoryStatValue - a model defined in Swagger"""  # noqa: E501

        self._time = None
        self._value = None
        self.discriminator = None

        self.time = time
        self.value = value

    @property
    def time(self):
        """Gets the time of this StatisticsHistoryStatValue.  # noqa: E501

        Unix Epoch time in seconds that statistic was collected.  # noqa: E501

        :return: The time of this StatisticsHistoryStatValue.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StatisticsHistoryStatValue.

        Unix Epoch time in seconds that statistic was collected.  # noqa: E501

        :param time: The time of this StatisticsHistoryStatValue.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def value(self):
        """Gets the value of this StatisticsHistoryStatValue.  # noqa: E501

        Key dependent value.  # noqa: E501

        :return: The value of this StatisticsHistoryStatValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StatisticsHistoryStatValue.

        Key dependent value.  # noqa: E501

        :param value: The value of this StatisticsHistoryStatValue.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, StatisticsHistoryStatValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other