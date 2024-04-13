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

from pluggy_sdk.models.payment_request_receipt_list200_response import PaymentRequestReceiptList200Response

class TestPaymentRequestReceiptList200Response(unittest.TestCase):
    """PaymentRequestReceiptList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentRequestReceiptList200Response:
        """Test PaymentRequestReceiptList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentRequestReceiptList200Response`
        """
        model = PaymentRequestReceiptList200Response()
        if include_optional:
            return PaymentRequestReceiptList200Response(
                page = 1.337,
                total = 1.337,
                total_pages = 1.337,
                results = [
                    {"amount":100.0,"creditor":{"bankAccount":{"branch":"0001","number":"123456","type":"CHECKING_ACCOUNT"},"name":"Creditor Name","taxNumber":"12345678901"},"date":"2020-04-21T15:00:00.000Z","debtor":{"bankAccount":{"branch":"0001","number":"123456","type":"CHECKING_ACCOUNT"},"name":"Debtor Name","taxNumber":"12345678901"},"description":"Payment description","expiresAt":"2020-04-21T15:00:00.000Z","id":"5e9f8f8f-f8f8-4f8f-8f8f-8f8f8f8f8f8f","paymentRequestId":"5e9f8f8f-f8f8-4f8f-8f8f-8f8f8f8f8f8f","receiptUrl":"https://example.com/receipt","referenceId":"123456"}
                    ]
            )
        else:
            return PaymentRequestReceiptList200Response(
        )
        """

    def testPaymentRequestReceiptList200Response(self):
        """Test PaymentRequestReceiptList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
