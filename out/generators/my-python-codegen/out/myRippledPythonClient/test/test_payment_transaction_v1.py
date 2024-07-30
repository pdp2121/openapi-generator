# coding: utf-8

"""
    XRP Ledger Public API

    A JSON RPC API used to query rippled.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.payment_transaction_v1 import PaymentTransactionV1

class TestPaymentTransactionV1(unittest.TestCase):
    """PaymentTransactionV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentTransactionV1:
        """Test PaymentTransactionV1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentTransactionV1`
        """
        model = PaymentTransactionV1()
        if include_optional:
            return PaymentTransactionV1(
                amount = None,
                transaction_type = '',
                deliver_min = None,
                destination = '',
                destination_tag = 56,
                invoice_id = '',
                paths = [
                    [
                        openapi_client.models.path.Path(
                            account = '', 
                            currency = '', 
                            issuer = '', 
                            type = 56, 
                            type_hex = '', )
                        ]
                    ],
                send_max = None,
                account = '',
                fee = '',
                sequence = 56,
                account_txn_id = '',
                flags = 56,
                last_ledger_sequence = 56,
                memos = [
                    None
                    ],
                network_id = 56,
                signers = [
                    None
                    ],
                source_tag = 56,
                signing_pub_key = '',
                ticket_sequence = 56,
                txn_signature = ''
            )
        else:
            return PaymentTransactionV1(
                amount = None,
                transaction_type = '',
                destination = '',
                account = '',
        )
        """

    def testPaymentTransactionV1(self):
        """Test PaymentTransactionV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
