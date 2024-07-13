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

from pluggy_sdk.api.payment_schedule_api import PaymentScheduleApi


class TestPaymentScheduleApi(unittest.TestCase):
    """PaymentScheduleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentScheduleApi()

    def tearDown(self) -> None:
        pass

    def test_payment_schedules_cancel(self) -> None:
        """Test case for payment_schedules_cancel

        Cancel Payment Schedule Authorization
        """
        pass

    def test_payment_schedules_cancel_specific(self) -> None:
        """Test case for payment_schedules_cancel_specific

        Cancel Payment Schedule Authorization
        """
        pass

    def test_payment_schedules_list(self) -> None:
        """Test case for payment_schedules_list

        Schedule List
        """
        pass


if __name__ == '__main__':
    unittest.main()
