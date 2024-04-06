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

from pluggy_sdk.models.parameter_validation_response import ParameterValidationResponse

class TestParameterValidationResponse(unittest.TestCase):
    """ParameterValidationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParameterValidationResponse:
        """Test ParameterValidationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParameterValidationResponse`
        """
        model = ParameterValidationResponse()
        if include_optional:
            return ParameterValidationResponse(
                errors = [
                    pluggy_sdk.models.parameter_validation_error.ParameterValidationError(
                        code = '', 
                        message = '', 
                        parameter = '', )
                    ],
                parameters = {"user":"my-user","password":"my-password"}
            )
        else:
            return ParameterValidationResponse(
        )
        """

    def testParameterValidationResponse(self):
        """Test ParameterValidationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
