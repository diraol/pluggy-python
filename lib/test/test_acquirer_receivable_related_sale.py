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

from pluggy_sdk.models.acquirer_receivable_related_sale import AcquirerReceivableRelatedSale

class TestAcquirerReceivableRelatedSale(unittest.TestCase):
    """AcquirerReceivableRelatedSale unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AcquirerReceivableRelatedSale:
        """Test AcquirerReceivableRelatedSale
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AcquirerReceivableRelatedSale`
        """
        model = AcquirerReceivableRelatedSale()
        if include_optional:
            return AcquirerReceivableRelatedSale(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                gross_amount = 1.337,
                net_amount = 1.337,
                installment_count = 1.337,
                installment_number = 1.337,
                nsu = ''
            )
        else:
            return AcquirerReceivableRelatedSale(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                gross_amount = 1.337,
                net_amount = 1.337,
                installment_count = 1.337,
                installment_number = 1.337,
                nsu = '',
        )
        """

    def testAcquirerReceivableRelatedSale(self):
        """Test AcquirerReceivableRelatedSale"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
