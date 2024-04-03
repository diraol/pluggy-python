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

from openapi_client.api.bulk_payment_api import BulkPaymentApi


class TestBulkPaymentApi(unittest.TestCase):
    """BulkPaymentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BulkPaymentApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_payment_create(self) -> None:
        """Test case for bulk_payment_create

        Create
        """
        pass

    def test_bulk_payment_retrieve(self) -> None:
        """Test case for bulk_payment_retrieve

        Retrieve
        """
        pass

    def test_bulk_payments_list(self) -> None:
        """Test case for bulk_payments_list

        List
        """
        pass


if __name__ == '__main__':
    unittest.main()
