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

from pluggy_sdk.models.custom import CUSTOM

class TestCUSTOM(unittest.TestCase):
    """CUSTOM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CUSTOM:
        """Test CUSTOM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CUSTOM`
        """
        model = CUSTOM()
        if include_optional:
            return CUSTOM(
                type = 'CUSTOM',
                dates = [
                    'Tue Jun 11 00:00:00 UTC 2024'
                    ],
                additional_information = ''
            )
        else:
            return CUSTOM(
                type = 'CUSTOM',
                dates = [
                    'Tue Jun 11 00:00:00 UTC 2024'
                    ],
        )
        """

    def testCUSTOM(self):
        """Test CUSTOM"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
