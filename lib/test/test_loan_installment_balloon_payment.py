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

from pluggy_sdk.models.loan_installment_balloon_payment import LoanInstallmentBalloonPayment

class TestLoanInstallmentBalloonPayment(unittest.TestCase):
    """LoanInstallmentBalloonPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoanInstallmentBalloonPayment:
        """Test LoanInstallmentBalloonPayment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoanInstallmentBalloonPayment`
        """
        model = LoanInstallmentBalloonPayment()
        if include_optional:
            return LoanInstallmentBalloonPayment(
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                amount = pluggy_sdk.models.loan_installment_balloon_payment_amount.LoanInstallmentBalloonPaymentAmount(
                    value = 1.337, 
                    currency_code = 'BRL', )
            )
        else:
            return LoanInstallmentBalloonPayment(
        )
        """

    def testLoanInstallmentBalloonPayment(self):
        """Test LoanInstallmentBalloonPayment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
