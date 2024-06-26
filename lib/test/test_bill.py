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

from pluggy_sdk.models.bill import Bill

class TestBill(unittest.TestCase):
    """Bill unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Bill:
        """Test Bill
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Bill`
        """
        model = Bill()
        if include_optional:
            return Bill(
                id = '',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                total_amount = 1.337,
                total_amount_currency_code = 'BRL',
                minimum_payment_amount = 1.337,
                allows_installments = True,
                finance_charges = [
                    {}
                    ]
            )
        else:
            return Bill(
                id = '',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                total_amount = 1.337,
                total_amount_currency_code = 'BRL',
                finance_charges = [
                    {}
                    ],
        )
        """

    def testBill(self):
        """Test Bill"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
