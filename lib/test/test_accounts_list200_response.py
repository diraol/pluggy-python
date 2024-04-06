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

from pluggy_sdk.models.accounts_list200_response import AccountsList200Response

class TestAccountsList200Response(unittest.TestCase):
    """AccountsList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountsList200Response:
        """Test AccountsList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountsList200Response`
        """
        model = AccountsList200Response()
        if include_optional:
            return AccountsList200Response(
                page = 1.337,
                total = 1.337,
                total_pages = 1.337,
                results = [
                    pluggy_sdk.models.account.Account(
                        id = 'a658c848-e475-457b-8565-d1fffba127c4', 
                        type = 'BANK', 
                        subtype = 'SAVINGS_ACCOUNT', 
                        number = '40114687/1234', 
                        name = 'Conta Corrente', 
                        marketing_name = 'SIGNATURE CJA. AHORRO PESOS', 
                        balance = 120950.0, 
                        item_id = 'a0922d6f-2007-4169-a181-b961500608db', 
                        tax_number = '416.799.495-00', 
                        owner = 'John Doe', 
                        currency_code = 'BRL', 
                        bank_data = pluggy_sdk.models.bank_data.BankData(
                            transfer_number = '', 
                            closing_balance = 1.337, 
                            automatically_invested_balance = 1.337, ), 
                        credit_data = pluggy_sdk.models.credit_data.CreditData(
                            level = '', 
                            brand = '', 
                            balance_close_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            balance_due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            available_credit_limit = 1.337, 
                            balance_foreign_currency = 1.337, 
                            minimum_payment = 1.337, 
                            credit_limit = 1.337, 
                            status = 'ACTIVE', 
                            holder_type = 'MAIN', ), )
                    ]
            )
        else:
            return AccountsList200Response(
        )
        """

    def testAccountsList200Response(self):
        """Test AccountsList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
