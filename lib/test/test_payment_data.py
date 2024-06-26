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

from pluggy_sdk.models.payment_data import PaymentData

class TestPaymentData(unittest.TestCase):
    """PaymentData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentData:
        """Test PaymentData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentData`
        """
        model = PaymentData()
        if include_optional:
            return PaymentData(
                payer = pluggy_sdk.models.payment_data_participant.PaymentDataParticipant(
                    document_number = pluggy_sdk.models.document.Document(
                        type = 'CPF', 
                        value = '416.799.495-00', ), 
                    name = '', 
                    account_number = '', 
                    branch_number = '', 
                    routing_number = '', 
                    routing_number_ispb = '', ),
                receiver = pluggy_sdk.models.payment_data_participant.PaymentDataParticipant(
                    document_number = pluggy_sdk.models.document.Document(
                        type = 'CPF', 
                        value = '416.799.495-00', ), 
                    name = '', 
                    account_number = '', 
                    branch_number = '', 
                    routing_number = '', 
                    routing_number_ispb = '', ),
                reason = '',
                reference_number = '',
                receiver_reference_id = '',
                payment_method = ''
            )
        else:
            return PaymentData(
        )
        """

    def testPaymentData(self):
        """Test PaymentData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
