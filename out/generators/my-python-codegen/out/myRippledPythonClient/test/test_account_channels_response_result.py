# coding: utf-8

"""
    XRP Ledger Public API

    A JSON RPC API used to query rippled.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.account_channels_response_result import AccountChannelsResponseResult

class TestAccountChannelsResponseResult(unittest.TestCase):
    """AccountChannelsResponseResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountChannelsResponseResult:
        """Test AccountChannelsResponseResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountChannelsResponseResult`
        """
        model = AccountChannelsResponseResult()
        if include_optional:
            return AccountChannelsResponseResult(
                account = '',
                channels = [
                    openapi_client.models.account_channels_response_result_channels_inner.AccountChannelsResponse_result_channels_inner(
                        channel_id = '', 
                        balance = '', )
                    ]
            )
        else:
            return AccountChannelsResponseResult(
        )
        """

    def testAccountChannelsResponseResult(self):
        """Test AccountChannelsResponseResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
