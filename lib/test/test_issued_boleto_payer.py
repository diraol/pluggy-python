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

from pluggy_sdk.models.issued_boleto_payer import IssuedBoletoPayer

class TestIssuedBoletoPayer(unittest.TestCase):
    """IssuedBoletoPayer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IssuedBoletoPayer:
        """Test IssuedBoletoPayer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IssuedBoletoPayer`
        """
        model = IssuedBoletoPayer()
        if include_optional:
            return IssuedBoletoPayer(
                tax_number = '',
                person_type = '',
                name = '',
                address_street = '',
                address_number = '',
                address_complement = '',
                address_neighborhood = '',
                address_city = '',
                address_state = '',
                address_zip_code = '',
                email = '',
                ddd = '',
                phone_number = ''
            )
        else:
            return IssuedBoletoPayer(
                tax_number = '',
                name = '',
                address_state = '',
                address_zip_code = '',
        )
        """

    def testIssuedBoletoPayer(self):
        """Test IssuedBoletoPayer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
