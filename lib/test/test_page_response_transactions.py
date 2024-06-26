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

from pluggy_sdk.models.page_response_transactions import PageResponseTransactions

class TestPageResponseTransactions(unittest.TestCase):
    """PageResponseTransactions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageResponseTransactions:
        """Test PageResponseTransactions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageResponseTransactions`
        """
        model = PageResponseTransactions()
        if include_optional:
            return PageResponseTransactions(
                results = [
                    {"id":"6ec156fe-e8ac-4d9a-a4b3-7770529ab01c","description":"TED Example","descriptionRaw":null,"currencyCode":"BRL","amount":1500,"date":"2020-10-14T00:00:00.000Z","balance":3500,"category":"Transfers","categoryId":"05000000","accountId":"03cc0eff-4ec5-495c-adb3-1ef9611624fc","providerCode":"123456","type":"CREDIT","status":"POSTED","paymentData":{"payer":{"name":"Tiago Rodrigues Santos","branchNumber":"090","accountNumber":"1234-5","routingNumber":"001","documentNumber":{"type":"CPF","value":"882.937.076-23"}},"reason":"Taxa de serviço","receiver":{"name":"Pluggy","branchNumber":"999","accountNumber":"9876-1","routingNumber":"002","documentNumber":{"type":"CNPJ","value":"08.050.608/0001-32"}},"paymentMethod":"TED","referenceNumber":"123456789"},"merchant":null}
                    ],
                page = 1.337,
                total = 1.337,
                total_pages = 1.337
            )
        else:
            return PageResponseTransactions(
                results = [
                    {"id":"6ec156fe-e8ac-4d9a-a4b3-7770529ab01c","description":"TED Example","descriptionRaw":null,"currencyCode":"BRL","amount":1500,"date":"2020-10-14T00:00:00.000Z","balance":3500,"category":"Transfers","categoryId":"05000000","accountId":"03cc0eff-4ec5-495c-adb3-1ef9611624fc","providerCode":"123456","type":"CREDIT","status":"POSTED","paymentData":{"payer":{"name":"Tiago Rodrigues Santos","branchNumber":"090","accountNumber":"1234-5","routingNumber":"001","documentNumber":{"type":"CPF","value":"882.937.076-23"}},"reason":"Taxa de serviço","receiver":{"name":"Pluggy","branchNumber":"999","accountNumber":"9876-1","routingNumber":"002","documentNumber":{"type":"CNPJ","value":"08.050.608/0001-32"}},"paymentMethod":"TED","referenceNumber":"123456789"},"merchant":null}
                    ],
                page = 1.337,
                total = 1.337,
                total_pages = 1.337,
        )
        """

    def testPageResponseTransactions(self):
        """Test PageResponseTransactions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
