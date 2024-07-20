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

from pluggy_sdk.models.monthly import MONTHLY

class TestMONTHLY(unittest.TestCase):
    """MONTHLY unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MONTHLY:
        """Test MONTHLY
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MONTHLY`
        """
        model = MONTHLY()
        if include_optional:
            return MONTHLY(
                type = 'MONTHLY',
                start_date = 'Tue Jun 11 00:00:00 UTC 2024',
                day_of_month = 3,
                occurrences = 3
            )
        else:
            return MONTHLY(
                type = 'MONTHLY',
                start_date = 'Tue Jun 11 00:00:00 UTC 2024',
                day_of_month = 3,
        )
        """

    def testMONTHLY(self):
        """Test MONTHLY"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()