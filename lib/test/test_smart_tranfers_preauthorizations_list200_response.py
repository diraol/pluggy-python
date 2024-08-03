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

from pluggy_sdk.models.smart_tranfers_preauthorizations_list200_response import SmartTranfersPreauthorizationsList200Response

class TestSmartTranfersPreauthorizationsList200Response(unittest.TestCase):
    """SmartTranfersPreauthorizationsList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartTranfersPreauthorizationsList200Response:
        """Test SmartTranfersPreauthorizationsList200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SmartTranfersPreauthorizationsList200Response`
        """
        model = SmartTranfersPreauthorizationsList200Response()
        if include_optional:
            return SmartTranfersPreauthorizationsList200Response(
                page = 1.337,
                total = 1.337,
                total_pages = 1.337,
                results = [
                    pluggy_sdk.models.smart_transfer_preauthorization.SmartTransferPreauthorization(
                        id = '', 
                        status = 'COMPLETED', 
                        consent_url = '', 
                        client_preauthorization_id = '', 
                        callback_urls = {}, 
                        recipients = [
                            {"id":"5e9f8f8f-f8f8-4f8f-8f8f-8f8f8f8f8f8f","name":"Conta empresa","taxNumber":"123456789-00","paymentInstitution":{"id":"00000000-0000-0000-0000-000000000000","name":"Banco J. Safra S.A.","ispb":"03017677","tradeName":"Banco Safra","compe":"074","createdAt":"2020-04-21T15:00:00.000Z","updatedAt":"2020-04-21T15:00:00.000Z"},"account":{"branch":"0001","number":"123456","type":"CHECKING_ACCOUNT"},"isDefault":true,"pixKey":null}
                            ], 
                        connector = {"id":601,"name":"Itaú","primaryColor":"EC7000","institutionUrl":"https://www.itau.com.br","country":"BR","type":"PERSONAL_BANK","credentials":[{"validation":"^\\d{3}\\.?\\d{3}\\.?\\d{3}-?\\d{2}$","validationMessage":"CPF deve ter 11 números.","label":"CPF","name":"cpf","type":"number","placeholder":"","optional":false}],"imageUrl":"https://cdn.pluggy.ai/assets/connector-icons/201.svg","hasMFA":false,"oauth":true,"health":{"status":"ONLINE","stage":null},"products":["ACCOUNTS","TRANSACTIONS","IDENTITY","CREDIT_CARDS","PAYMENT_DATA","LOANS","INVESTMENTS"],"createdAt":"2023-09-01T18:05:09.145Z","isSandbox":false,"isOpenFinance":true,"updatedAt":"2024-07-16T15:34:08.028Z","supportsPaymentInitiation":true,"supportsScheduledPayments":true,"supportsSmartTransfers":true}, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return SmartTranfersPreauthorizationsList200Response(
        )
        """

    def testSmartTranfersPreauthorizationsList200Response(self):
        """Test SmartTranfersPreauthorizationsList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
