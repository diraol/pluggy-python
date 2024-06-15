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

from pluggy_sdk.models.schedule_type_daily import ScheduleTypeDaily

class TestScheduleTypeDaily(unittest.TestCase):
    """ScheduleTypeDaily unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleTypeDaily:
        """Test ScheduleTypeDaily
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleTypeDaily`
        """
        model = ScheduleTypeDaily()
        if include_optional:
            return ScheduleTypeDaily(
                type = 'DAILY',
                start_date = 'Tue Jun 11 00:00:00 UTC 2024',
                quantity = 3
            )
        else:
            return ScheduleTypeDaily(
                type = 'DAILY',
                start_date = 'Tue Jun 11 00:00:00 UTC 2024',
                quantity = 3,
        )
        """

    def testScheduleTypeDaily(self):
        """Test ScheduleTypeDaily"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
