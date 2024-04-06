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

from pluggy_sdk.models.acquirer_sale_data import AcquirerSaleData

class TestAcquirerSaleData(unittest.TestCase):
    """AcquirerSaleData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AcquirerSaleData:
        """Test AcquirerSaleData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AcquirerSaleData`
        """
        model = AcquirerSaleData()
        if include_optional:
            return AcquirerSaleData(
                nsu = '',
                authorization_code = '',
                payment_method = 'CARD',
                net_amount = 1.337,
                mdr_fee = 1.337,
                mdr_fee_amount = 1.337,
                status = 'APPROVED',
                installment_count = 1.337,
                installments = [
                    pluggy_sdk.models.acquirer_sale_installment.AcquirerSaleInstallment(
                        number = 1.337, 
                        net_amount = 1.337, 
                        receipt_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                card_flag = '',
                card_number = '',
                card_funding_source = 'CREDIT',
                terminal_id = ''
            )
        else:
            return AcquirerSaleData(
                nsu = '',
        )
        """

    def testAcquirerSaleData(self):
        """Test AcquirerSaleData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
