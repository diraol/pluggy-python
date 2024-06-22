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

from pluggy_sdk.models.payroll_loan import PayrollLoan

class TestPayrollLoan(unittest.TestCase):
    """PayrollLoan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayrollLoan:
        """Test PayrollLoan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayrollLoan`
        """
        model = PayrollLoan()
        if include_optional:
            return PayrollLoan(
                contract_code = '',
                cnpj_original_contract_creditor = '',
                nominal_interest_rate = 1.337,
                efective_interest_rate = 1.337,
                cet_annual_rate = 1.337,
                cet_month_rate = 1.337,
                currency_code = 'BRL',
                amortization_regime = '',
                installments_quantity = 1.337,
                installments_value = 1.337,
                due_date_first_installment = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                due_date_last_installment = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                cnpj_correspondent_banking = '',
                operation_hiring_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                client = pluggy_sdk.models.payroll_loan_client.PayrollLoan_client(
                    name = '', 
                    document = '', 
                    phone = '', 
                    addres_street = '', 
                    address_number = '', 
                    address_city = '', 
                    address_zip_code = '', 
                    address_state = '', )
            )
        else:
            return PayrollLoan(
                contract_code = '',
                client = pluggy_sdk.models.payroll_loan_client.PayrollLoan_client(
                    name = '', 
                    document = '', 
                    phone = '', 
                    addres_street = '', 
                    address_number = '', 
                    address_city = '', 
                    address_zip_code = '', 
                    address_state = '', ),
        )
        """

    def testPayrollLoan(self):
        """Test PayrollLoan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
