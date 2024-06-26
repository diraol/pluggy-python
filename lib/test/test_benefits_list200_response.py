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

from pluggy_sdk.models.benefits_list200_response import BenefitsList200Response

class TestBenefitsList200Response(unittest.TestCase):
    """BenefitsList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BenefitsList200Response:
        """Test BenefitsList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BenefitsList200Response`
        """
        model = BenefitsList200Response()
        if include_optional:
            return BenefitsList200Response(
                page = 1.337,
                total = 1.337,
                total_pages = 1.337,
                results = [
                    {}
                    ]
            )
        else:
            return BenefitsList200Response(
        )
        """

    def testBenefitsList200Response(self):
        """Test BenefitsList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
