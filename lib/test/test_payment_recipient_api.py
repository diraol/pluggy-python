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

from pluggy_sdk.api.payment_recipient_api import PaymentRecipientApi


class TestPaymentRecipientApi(unittest.TestCase):
    """PaymentRecipientApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentRecipientApi()

    def tearDown(self) -> None:
        pass

    def test_payment_recipient_create(self) -> None:
        """Test case for payment_recipient_create

        Create
        """
        pass

    def test_payment_recipient_delete(self) -> None:
        """Test case for payment_recipient_delete

        Delete
        """
        pass

    def test_payment_recipient_institutions_retrieve(self) -> None:
        """Test case for payment_recipient_institutions_retrieve

        Retrieve Institution
        """
        pass

    def test_payment_recipient_retrieve(self) -> None:
        """Test case for payment_recipient_retrieve

        Retrieve
        """
        pass

    def test_payment_recipient_update(self) -> None:
        """Test case for payment_recipient_update

        Update
        """
        pass

    def test_payment_recipients_institution_list(self) -> None:
        """Test case for payment_recipients_institution_list

        List Institutions
        """
        pass

    def test_payment_recipients_list(self) -> None:
        """Test case for payment_recipients_list

        List
        """
        pass


if __name__ == '__main__':
    unittest.main()
