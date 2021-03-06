# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 4
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_0_1
from isi_sdk_8_0_1.api.hardware_api import HardwareApi  # noqa: E501
from isi_sdk_8_0_1.rest import ApiException


class TestHardwareApi(unittest.TestCase):
    """HardwareApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_0_1.api.hardware_api.HardwareApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_hardware_tape_name(self):
        """Test case for create_hardware_tape_name

        """
        pass

    def test_delete_hardware_tape_name(self):
        """Test case for delete_hardware_tape_name

        """
        pass

    def test_get_hardware_fcport(self):
        """Test case for get_hardware_fcport

        """
        pass

    def test_get_hardware_fcports(self):
        """Test case for get_hardware_fcports

        """
        pass

    def test_get_hardware_tapes(self):
        """Test case for get_hardware_tapes

        """
        pass

    def test_update_hardware_fcport(self):
        """Test case for update_hardware_fcport

        """
        pass

    def test_update_hardware_tape_name(self):
        """Test case for update_hardware_tape_name

        """
        pass


if __name__ == '__main__':
    unittest.main()
