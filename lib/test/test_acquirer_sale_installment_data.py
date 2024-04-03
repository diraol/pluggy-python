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

from openapi_client.models.acquirer_sale_installment_data import AcquirerSaleInstallmentData

class TestAcquirerSaleInstallmentData(unittest.TestCase):
    """AcquirerSaleInstallmentData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AcquirerSaleInstallmentData:
        """Test AcquirerSaleInstallmentData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AcquirerSaleInstallmentData`
        """
        model = AcquirerSaleInstallmentData()
        if include_optional:
            return AcquirerSaleInstallmentData(
                number = 1.337,
                gross_amount = 1.337,
                net_amount = 1.337,
                receipt_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return AcquirerSaleInstallmentData(
                number = 1.337,
                gross_amount = 1.337,
        )
        """

    def testAcquirerSaleInstallmentData(self):
        """Test AcquirerSaleInstallmentData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
