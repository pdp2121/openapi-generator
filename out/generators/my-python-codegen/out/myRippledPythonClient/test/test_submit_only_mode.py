# coding: utf-8

"""
    XRP Ledger Public API

    A JSON RPC API used to query rippled.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.submit_only_mode import SubmitOnlyMode

class TestSubmitOnlyMode(unittest.TestCase):
    """SubmitOnlyMode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubmitOnlyMode:
        """Test SubmitOnlyMode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubmitOnlyMode`
        """
        model = SubmitOnlyMode()
        if include_optional:
            return SubmitOnlyMode(
                tx_blob = '',
                fail_hard = True
            )
        else:
            return SubmitOnlyMode(
                tx_blob = '',
        )
        """

    def testSubmitOnlyMode(self):
        """Test SubmitOnlyMode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
