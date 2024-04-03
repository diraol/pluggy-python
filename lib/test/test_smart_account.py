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

from openapi_client.models.smart_account import SmartAccount

class TestSmartAccount(unittest.TestCase):
    """SmartAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartAccount:
        """Test SmartAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SmartAccount`
        """
        model = SmartAccount()
        if include_optional:
            return SmartAccount(
                id = '',
                ispb = '',
                agency = '',
                number = '',
                verifying_digit = '',
                type = 'CHECKING_ACCOUNT',
                is_sandbox = True
            )
        else:
            return SmartAccount(
                id = '',
                ispb = '',
                agency = '',
                number = '',
                verifying_digit = '',
                type = 'CHECKING_ACCOUNT',
                is_sandbox = True,
        )
        """

    def testSmartAccount(self):
        """Test SmartAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
