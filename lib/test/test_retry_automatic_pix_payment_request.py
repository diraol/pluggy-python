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

from pluggy_sdk.models.retry_automatic_pix_payment_request import RetryAutomaticPixPaymentRequest

class TestRetryAutomaticPixPaymentRequest(unittest.TestCase):
    """RetryAutomaticPixPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetryAutomaticPixPaymentRequest:
        """Test RetryAutomaticPixPaymentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetryAutomaticPixPaymentRequest`
        """
        model = RetryAutomaticPixPaymentRequest()
        if include_optional:
            return RetryAutomaticPixPaymentRequest(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return RetryAutomaticPixPaymentRequest(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testRetryAutomaticPixPaymentRequest(self):
        """Test RetryAutomaticPixPaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
