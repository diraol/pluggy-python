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

from pluggy_sdk.api.boleto_management_api import BoletoManagementApi


class TestBoletoManagementApi(unittest.TestCase):
    """BoletoManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BoletoManagementApi()

    def tearDown(self) -> None:
        pass

    def test_boleto_cancel(self) -> None:
        """Test case for boleto_cancel

        Cancel Boleto
        """
        pass

    def test_boleto_connection_create(self) -> None:
        """Test case for boleto_connection_create

        Connect boleto credentials
        """
        pass

    def test_boleto_create(self) -> None:
        """Test case for boleto_create

        Issue Boleto
        """
        pass


if __name__ == '__main__':
    unittest.main()
