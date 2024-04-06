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

from pluggy_sdk.models.identity_response import IdentityResponse

class TestIdentityResponse(unittest.TestCase):
    """IdentityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityResponse:
        """Test IdentityResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityResponse`
        """
        model = IdentityResponse()
        if include_optional:
            return IdentityResponse(
                id = '',
                item_id = '',
                birth_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tax_number = '',
                document = '',
                document_type = '',
                job_title = '',
                full_name = '',
                establishment_code = '',
                establishment_name = '',
                company_name = '',
                phone_numbers = [
                    pluggy_sdk.models.phone_number.PhoneNumber(
                        type = 'Personal', 
                        value = '', )
                    ],
                emails = [
                    pluggy_sdk.models.email.Email(
                        type = 'Personal', 
                        value = '', )
                    ],
                addresses = [
                    pluggy_sdk.models.address.Address(
                        full_address = '', 
                        primary_address = '', 
                        city = '', 
                        postal_code = '', 
                        state = '', 
                        country = '', 
                        type = 'Personal', )
                    ],
                relations = [
                    pluggy_sdk.models.identity_relation.IdentityRelation(
                        type = 'Mother', 
                        name = '', 
                        document = '', )
                    ]
            )
        else:
            return IdentityResponse(
                id = '',
                item_id = '',
        )
        """

    def testIdentityResponse(self):
        """Test IdentityResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
