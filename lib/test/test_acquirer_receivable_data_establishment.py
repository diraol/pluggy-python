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

from pluggy_sdk.models.acquirer_receivable_data_establishment import AcquirerReceivableDataEstablishment

class TestAcquirerReceivableDataEstablishment(unittest.TestCase):
    """AcquirerReceivableDataEstablishment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AcquirerReceivableDataEstablishment:
        """Test AcquirerReceivableDataEstablishment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AcquirerReceivableDataEstablishment`
        """
        model = AcquirerReceivableDataEstablishment()
        if include_optional:
            return AcquirerReceivableDataEstablishment(
                company_code = '',
                company_name = '',
                receiving_bank = '',
                agency = '',
                account = ''
            )
        else:
            return AcquirerReceivableDataEstablishment(
        )
        """

    def testAcquirerReceivableDataEstablishment(self):
        """Test AcquirerReceivableDataEstablishment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
