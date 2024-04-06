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

from pluggy_sdk.models.connector_health_details import ConnectorHealthDetails

class TestConnectorHealthDetails(unittest.TestCase):
    """ConnectorHealthDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectorHealthDetails:
        """Test ConnectorHealthDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectorHealthDetails`
        """
        model = ConnectorHealthDetails()
        if include_optional:
            return ConnectorHealthDetails(
                connection_rate_last6_hours = 1.337,
                connections_last6_hours = 1.337
            )
        else:
            return ConnectorHealthDetails(
        )
        """

    def testConnectorHealthDetails(self):
        """Test ConnectorHealthDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
