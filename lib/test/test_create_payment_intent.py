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

from pluggy_sdk.models.create_payment_intent import CreatePaymentIntent

class TestCreatePaymentIntent(unittest.TestCase):
    """CreatePaymentIntent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePaymentIntent:
        """Test CreatePaymentIntent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePaymentIntent`
        """
        model = CreatePaymentIntent()
        if include_optional:
            return CreatePaymentIntent(
                payment_request_id = '',
                bulk_payment_id = '',
                connector_id = 1.337,
                parameters = {"user":"my-user","password":"my-password"}
            )
        else:
            return CreatePaymentIntent(
                connector_id = 1.337,
                parameters = {"user":"my-user","password":"my-password"},
        )
        """

    def testCreatePaymentIntent(self):
        """Test CreatePaymentIntent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
