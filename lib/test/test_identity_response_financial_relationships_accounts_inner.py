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

from pluggy_sdk.models.identity_response_financial_relationships_accounts_inner import IdentityResponseFinancialRelationshipsAccountsInner

class TestIdentityResponseFinancialRelationshipsAccountsInner(unittest.TestCase):
    """IdentityResponseFinancialRelationshipsAccountsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityResponseFinancialRelationshipsAccountsInner:
        """Test IdentityResponseFinancialRelationshipsAccountsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityResponseFinancialRelationshipsAccountsInner`
        """
        model = IdentityResponseFinancialRelationshipsAccountsInner()
        if include_optional:
            return IdentityResponseFinancialRelationshipsAccountsInner(
                compe_code = '',
                branch_code = '',
                number = '',
                check_digit = '',
                type = '',
                subtype = ''
            )
        else:
            return IdentityResponseFinancialRelationshipsAccountsInner(
                compe_code = '',
                branch_code = '',
                number = '',
                check_digit = '',
                type = '',
                subtype = '',
        )
        """

    def testIdentityResponseFinancialRelationshipsAccountsInner(self):
        """Test IdentityResponseFinancialRelationshipsAccountsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
