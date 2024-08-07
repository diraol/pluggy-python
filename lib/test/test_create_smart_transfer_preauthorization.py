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

from pluggy_sdk.models.create_smart_transfer_preauthorization import CreateSmartTransferPreauthorization

class TestCreateSmartTransferPreauthorization(unittest.TestCase):
    """CreateSmartTransferPreauthorization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSmartTransferPreauthorization:
        """Test CreateSmartTransferPreauthorization
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSmartTransferPreauthorization`
        """
        model = CreateSmartTransferPreauthorization()
        if include_optional:
            return CreateSmartTransferPreauthorization(
                connector_id = '',
                parameters = {"cpf":"416.799.495-00","cnpj":"41.679.495/0001-00"},
                recipient_ids = [
                    ''
                    ],
                callback_urls = {},
                client_preauthorization_id = ''
            )
        else:
            return CreateSmartTransferPreauthorization(
                connector_id = '',
                parameters = {"cpf":"416.799.495-00","cnpj":"41.679.495/0001-00"},
                recipient_ids = [
                    ''
                    ],
        )
        """

    def testCreateSmartTransferPreauthorization(self):
        """Test CreateSmartTransferPreauthorization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
