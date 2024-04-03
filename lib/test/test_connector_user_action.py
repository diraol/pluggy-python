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

from openapi_client.models.connector_user_action import ConnectorUserAction

class TestConnectorUserAction(unittest.TestCase):
    """ConnectorUserAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectorUserAction:
        """Test ConnectorUserAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectorUserAction`
        """
        model = ConnectorUserAction()
        if include_optional:
            return ConnectorUserAction(
                instructions = '',
                attributes = None,
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ConnectorUserAction(
                instructions = '',
        )
        """

    def testConnectorUserAction(self):
        """Test ConnectorUserAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
