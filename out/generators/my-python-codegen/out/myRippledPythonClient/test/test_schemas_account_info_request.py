# coding: utf-8

"""
    XRP Ledger Public API

    A JSON RPC API used to query rippled.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.schemas_account_info_request import SchemasAccountInfoRequest

class TestSchemasAccountInfoRequest(unittest.TestCase):
    """SchemasAccountInfoRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchemasAccountInfoRequest:
        """Test SchemasAccountInfoRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchemasAccountInfoRequest`
        """
        model = SchemasAccountInfoRequest()
        if include_optional:
            return SchemasAccountInfoRequest(
                method = 'account_info',
                params = [
                    openapi_client.models.account_info_request.AccountInfoRequest(
                        account = '', 
                        queue = True, 
                        signer_lists = True, )
                    ]
            )
        else:
            return SchemasAccountInfoRequest(
                method = 'account_info',
        )
        """

    def testSchemasAccountInfoRequest(self):
        """Test SchemasAccountInfoRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
