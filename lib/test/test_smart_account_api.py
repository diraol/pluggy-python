# coding: utf-8

"""
    Pluggy API

    Pluggy's main API to review data and execute connectors

    The version of the OpenAPI document: 1.0.0
    Contact: hello@pluggy.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.smart_account_api import SmartAccountApi


class TestSmartAccountApi(unittest.TestCase):
    """SmartAccountApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SmartAccountApi()

    def tearDown(self) -> None:
        pass

    def test_smart_account_balance_retrieve(self) -> None:
        """Test case for smart_account_balance_retrieve

        Retrieve Balance
        """
        pass

    def test_smart_account_create(self) -> None:
        """Test case for smart_account_create

        Create
        """
        pass

    def test_smart_account_retrieve(self) -> None:
        """Test case for smart_account_retrieve

        Retrieve
        """
        pass

    def test_smart_accounts_list(self) -> None:
        """Test case for smart_accounts_list

        List
        """
        pass


if __name__ == '__main__':
    unittest.main()
