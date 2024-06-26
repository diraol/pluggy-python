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

from pluggy_sdk.models.loan_installment_balloon_payment_amount import LoanInstallmentBalloonPaymentAmount

class TestLoanInstallmentBalloonPaymentAmount(unittest.TestCase):
    """LoanInstallmentBalloonPaymentAmount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoanInstallmentBalloonPaymentAmount:
        """Test LoanInstallmentBalloonPaymentAmount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoanInstallmentBalloonPaymentAmount`
        """
        model = LoanInstallmentBalloonPaymentAmount()
        if include_optional:
            return LoanInstallmentBalloonPaymentAmount(
                value = 1.337,
                currency_code = 'BRL'
            )
        else:
            return LoanInstallmentBalloonPaymentAmount(
        )
        """

    def testLoanInstallmentBalloonPaymentAmount(self):
        """Test LoanInstallmentBalloonPaymentAmount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
