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

from openapi_client.models.update_item_parameters import UpdateItemParameters

class TestUpdateItemParameters(unittest.TestCase):
    """UpdateItemParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateItemParameters:
        """Test UpdateItemParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateItemParameters`
        """
        model = UpdateItemParameters()
        if include_optional:
            return UpdateItemParameters(
            )
        else:
            return UpdateItemParameters(
        )
        """

    def testUpdateItemParameters(self):
        """Test UpdateItemParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
