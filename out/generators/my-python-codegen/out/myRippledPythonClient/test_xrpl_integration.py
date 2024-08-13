import unittest
from xrpl.clients.json_rpc_client import JsonRpcClient
from openapi_client.models import AccountInfoRequest, SubmitOnlyMode, LookupByLedgerRequestLedgerIndex
from xrpl.wallet import generate_faucet_wallet
from xrpl.transaction import autofill, sign
from xrpl.models.transactions import Payment

class IntegrationTestAccountInfoRequest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")
        cls.test_wallet = generate_faucet_wallet(cls.client)

    def test_account_info_request(self):
        ledger_index = LookupByLedgerRequestLedgerIndex(actual_instance="current")

        # Create an AccountInfo request
        account_info_request = AccountInfoRequest(
            account=self.test_wallet.classic_address,
            strict=True,
            ledger_index=ledger_index,
            queue=True,
        )

        response = self.client.request(account_info_request)
        print(response.result)

        self.assertTrue(response.is_successful())
        self.assertIn("account_data", response.result)
        self.assertEqual(response.result["account_data"]["Account"], self.test_wallet.classic_address)
    
    def test_submit_transaction(self):
        # Initial account info request to get starting balance
        initial_response = self.client.request(AccountInfoRequest(
            account=self.test_wallet.classic_address,
            ledger_index=LookupByLedgerRequestLedgerIndex(actual_instance="current")
        ))
        initial_balance = int(initial_response.result["account_data"]["Balance"])

        # Send a payment to another account
        destination_address = "rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe"
        payment = Payment(
            account=self.test_wallet.classic_address,
            destination=destination_address,
            amount="10"
        )

        prepared = autofill(payment, self.client)

        signed = sign(prepared, self.test_wallet).blob()

        print ("Signed payment")
        print(signed)

        response = self.client.request(SubmitOnlyMode(tx_blob = signed))

        print(response.result)

        self.assertTrue(response.is_successful())

        final_response = self.client.request(AccountInfoRequest(
            account=self.test_wallet.classic_address,
            ledger_index=LookupByLedgerRequestLedgerIndex(actual_instance="current")
        ))
        final_balance = int(final_response.result["account_data"]["Balance"])

        self.assertTrue(final_balance < initial_balance)

if __name__ == '__main__':
    unittest.main()
