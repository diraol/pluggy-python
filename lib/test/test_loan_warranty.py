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

from pluggy_sdk.models.loan_warranty import LoanWarranty

class TestLoanWarranty(unittest.TestCase):
    """LoanWarranty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoanWarranty:
        """Test LoanWarranty
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoanWarranty`
        """
        model = LoanWarranty()
        if include_optional:
            return LoanWarranty(
                currency_code = 'BRL',
                type = '',
                subtype = '',
                amount = 1.337
            )
        else:
            return LoanWarranty(
        )
        """

    def testLoanWarranty(self):
        """Test LoanWarranty"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
