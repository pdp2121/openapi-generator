# coding: utf-8

"""
    XRP Ledger Public API

    A JSON RPC API used to query rippled.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.signer_list import SignerList

class TestSignerList(unittest.TestCase):
    """SignerList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignerList:
        """Test SignerList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignerList`
        """
        model = SignerList()
        if include_optional:
            return SignerList(
                ledger_entry_type = '',
                owner_node = '',
                previous_txn_id = '',
                previous_txn_lgr_seq = 56,
                signer_entries = [
                    openapi_client.models.signer_entry.SignerEntry(
                        account = '', 
                        signer_weight = 1.337, 
                        wallet_locator = '', )
                    ],
                signer_list_id = 56,
                signer_quorum = 56
            )
        else:
            return SignerList(
                ledger_entry_type = '',
                owner_node = '',
                previous_txn_id = '',
                previous_txn_lgr_seq = 56,
                signer_entries = [
                    openapi_client.models.signer_entry.SignerEntry(
                        account = '', 
                        signer_weight = 1.337, 
                        wallet_locator = '', )
                    ],
                signer_list_id = 56,
                signer_quorum = 56,
        )
        """

    def testSignerList(self):
        """Test SignerList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
