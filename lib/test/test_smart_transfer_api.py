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

from pluggy_sdk.api.smart_transfer_api import SmartTransferApi


class TestSmartTransferApi(unittest.TestCase):
    """SmartTransferApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SmartTransferApi()

    def tearDown(self) -> None:
        pass

    def test_smart_tranfers_preauthorizations_list(self) -> None:
        """Test case for smart_tranfers_preauthorizations_list

        List preauthorizations
        """
        pass

    def test_smart_transfer_payment_create(self) -> None:
        """Test case for smart_transfer_payment_create

        Create payment
        """
        pass

    def test_smart_transfer_paymentretrieve(self) -> None:
        """Test case for smart_transfer_paymentretrieve

        Retrieve payment
        """
        pass

    def test_smart_transfer_preauthorization_create(self) -> None:
        """Test case for smart_transfer_preauthorization_create

        Create preauthorization
        """
        pass

    def test_smart_transfer_preauthorization_retrieve(self) -> None:
        """Test case for smart_transfer_preauthorization_retrieve

        Retrieve preauthorization
        """
        pass


if __name__ == '__main__':
    unittest.main()