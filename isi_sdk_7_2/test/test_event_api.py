# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_7_2
from isi_sdk_7_2.api.event_api import EventApi  # noqa: E501
from isi_sdk_7_2.rest import ApiException


class TestEventApi(unittest.TestCase):
    """EventApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_7_2.api.event_api.EventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_event_event(self):
        """Test case for get_event_event

        """
        pass

    def test_get_event_events(self):
        """Test case for get_event_events

        """
        pass


if __name__ == '__main__':
    unittest.main()