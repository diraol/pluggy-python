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

from openapi_client.api.payment_customer_api import PaymentCustomerApi


class TestPaymentCustomerApi(unittest.TestCase):
    """PaymentCustomerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentCustomerApi()

    def tearDown(self) -> None:
        pass

    def test_payment_customer_create(self) -> None:
        """Test case for payment_customer_create

        Create
        """
        pass

    def test_payment_customer_delete(self) -> None:
        """Test case for payment_customer_delete

        Delete
        """
        pass

    def test_payment_customer_retrieve(self) -> None:
        """Test case for payment_customer_retrieve

        Retrieve
        """
        pass

    def test_payment_customer_update(self) -> None:
        """Test case for payment_customer_update

        Update
        """
        pass

    def test_payment_customers_list(self) -> None:
        """Test case for payment_customers_list

        List
        """
        pass


if __name__ == '__main__':
    unittest.main()
