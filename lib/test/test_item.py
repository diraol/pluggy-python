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

from openapi_client.models.item import Item

class TestItem(unittest.TestCase):
    """Item unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Item:
        """Test Item
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Item`
        """
        model = Item()
        if include_optional:
            return Item(
                id = '',
                connector = {"id":201,"name":"Itaú","primaryColor":"EC7000","institutionUrl":"https://www.itau.com.br","country":"BR","type":"PERSONAL_BANK","credentials":[{"label":"Agência","name":"agency","type":"number","placeholder":"Agência","validation":"^\\d{4}$","validationMessage":"O agencia deve ter 4 dígito"},{"label":"Conta","name":"account","type":"number","placeholder":"Conta","validation":"^\\d{4,6}$","validationMessage":"O conta deve ter 6 dígito"},{"label":"Senha","name":"password","type":"number","placeholder":"Senha","validation":"^\\d{6}$","validationMessage":"O senha deve ter 6 dígito"}],"imageUrl":"https://res.cloudinary.com/dkr0vihmp/image/upload/v1588853552/connectors-logos/itau_ntodvn.png","hasMFA":false,"products":["ACCOUNTS","TRANSACTIONS","CREDIT_CARDS","INVESTMENTS","IDENTITY","PAYMENT_DATA"],"oauthUrl":"https://example-oauth-url.com"},
                status = '',
                execution_status = '',
                error = openapi_client.models.item_error.Item_error(
                    code = '', 
                    message = '', 
                    provider_message = '', 
                    attributes = openapi_client.models.attributes.attributes(), ),
                parameter = openapi_client.models.connector_credential.ConnectorCredential(
                    name = '', 
                    label = '', 
                    type = 'text', 
                    assistive_text = '', 
                    data = '', 
                    placeholder = '', 
                    validation = '', 
                    validation_message = '', 
                    mfa = True, 
                    options = [
                        openapi_client.models.credential_select_option.CredentialSelectOption(
                            value = '', 
                            label = '', )
                        ], ),
                user_action = openapi_client.models.connector_user_action.ConnectorUserAction(
                    instructions = '', 
                    attributes = openapi_client.models.attributes.attributes(), 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                webhook_url = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status_detail = {"accounts":{"isUpdated":true,"lastUpdatedAt":"2022-03-08T22:43:04.796Z"},"identity":{"isUpdated":false,"lastUpdatedAt":null},"creditCards":{"isUpdated":true,"lastUpdatedAt":"2022-03-08T22:43:04.796Z"},"investments":{"isUpdated":true,"lastUpdatedAt":"2022-03-08T22:43:04.796Z"},"transactions":{"isUpdated":true,"lastUpdatedAt":"2022-03-08T22:43:04.796Z"},"paymentData":null},
                next_auto_sync_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                consecutive_failed_login_attempts = 1.337,
                products = [
                    'ACCOUNTS'
                    ]
            )
        else:
            return Item(
                id = '',
                status = '',
                execution_status = '',
        )
        """

    def testItem(self):
        """Test Item"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
