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

from pluggy_sdk.models.payment_customers_list200_response import PaymentCustomersList200Response

class TestPaymentCustomersList200Response(unittest.TestCase):
    """PaymentCustomersList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentCustomersList200Response:
        """Test PaymentCustomersList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentCustomersList200Response`
        """
        model = PaymentCustomersList200Response()
        if include_optional:
            return PaymentCustomersList200Response(
                page = 1.337,
                total = 1.337,
                total_pages = 1.337,
                results = [
                    {"id":"5e9f8f8f-f8f8-4f8f-8f8f-8f8f8f8f8f8f","type":"INDIVIDUAL","name":"Marco Silva","email":"msilva@pluggy.ai","cpf":"123456789-00"}
                    ]
            )
        else:
            return PaymentCustomersList200Response(
        )
        """

    def testPaymentCustomersList200Response(self):
        """Test PaymentCustomersList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
