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

from openapi_client.api.connector_api import ConnectorApi


class TestConnectorApi(unittest.TestCase):
    """ConnectorApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorApi()

    def tearDown(self) -> None:
        pass

    def test_connector_retrieve(self) -> None:
        """Test case for connector_retrieve

        Retrieve
        """
        pass

    def test_connectors_list(self) -> None:
        """Test case for connectors_list

        List
        """
        pass

    def test_connectors_validate(self) -> None:
        """Test case for connectors_validate

        Validate
        """
        pass


if __name__ == '__main__':
    unittest.main()
