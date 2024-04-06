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

from pluggy_sdk.models.payment_requests_list200_response import PaymentRequestsList200Response

class TestPaymentRequestsList200Response(unittest.TestCase):
    """PaymentRequestsList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentRequestsList200Response:
        """Test PaymentRequestsList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentRequestsList200Response`
        """
        model = PaymentRequestsList200Response()
        if include_optional:
            return PaymentRequestsList200Response(
                page = 1.337,
                total = 1.337,
                total_pages = 1.337,
                results = [
                    {}
                    ]
            )
        else:
            return PaymentRequestsList200Response(
        )
        """

    def testPaymentRequestsList200Response(self):
        """Test PaymentRequestsList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
