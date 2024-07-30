# PaymentTransactionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type** | **str** |  | 
**deliver_min** | [**CurrencyAmount**](CurrencyAmount.md) | (Optional) Minimum amount of destination currency this transaction should deliver. Only valid if this is a partial payment. For non-XRP amounts, the nested field names are lower-case. | [optional] 
**destination** | **str** | The unique address of the account receiving the payment. | 
**destination_tag** | **int** | (Optional) Arbitrary tag that identifies the reason for the payment to the destination, or a hosted recipient to pay. | [optional] 
**invoice_id** | **str** | (Optional) Arbitrary 256-bit hash representing a specific reason or identifier for this payment. | [optional] 
**paths** | **List[List[Path]]** | (Optional, auto-fillable) Array of payment paths to be used for this transaction. Must be omitted for XRP-to-XRP transactions. | [optional] 
**send_max** | [**CurrencyAmount**](CurrencyAmount.md) | (Optional) Highest amount of source currency this transaction is allowed to cost, including transfer fees, exchange rates, and slippage. Does not include the XRP destroyed as a cost for submitting the transaction. For non-XRP amounts, the nested field names MUST be lower-case. Must be supplied for cross-currency/cross-issue payments. Must be omitted for XRP-to-XRP payments. | [optional] 
**account** | **str** | The unique address of the account that initiated the transaction. | 
**fee** | **str** | Integer amount of XRP, in drops, to be destroyed as a cost for distributing this transaction to the network. Some transaction types have different minimum requirements. See Transaction Cost for details. | [optional] 
**sequence** | **int** | The sequence number of the account sending the transaction. A transaction is only valid if the Sequence number is exactly 1 greater than the previous transaction from the same account. The special case 0 means the transaction is using a Ticket instead. | [optional] 
**account_txn_id** | **str** | Hash value identifying another transaction. If provided, this transaction is only valid if the sending account&#39;s previously-sent transaction matches the provided hash. | [optional] 
**flags** | **int** | Set of bit-flags for this transaction. | [optional] 
**last_ledger_sequence** | **int** | Highest ledger index this transaction can appear in. Specifying this field places a strict upper limit on how long the transaction can wait to be validated or rejected. | [optional] 
**memos** | **List[object]** | Additional arbitrary information used to identify this transaction. | [optional] 
**network_id** | **int** | The network ID of the chain this transaction is intended for. MUST BE OMITTED for Mainnet and some test networks. REQUIRED on chains whose network ID is 1025 or higher. | [optional] 
**signers** | **List[object]** | Array of objects that represent a multi-signature which authorizes this transaction. | [optional] 
**source_tag** | **int** | Arbitrary integer used to identify the reason for this payment, or a sender on whose behalf this transaction is made. | [optional] 
**signing_pub_key** | **str** | Hex representation of the public key that corresponds to the private key used to sign this transaction. If an empty string, indicates a multi-signature is present in the Signers field instead. | [optional] 
**ticket_sequence** | **int** | The sequence number of the ticket to use in place of a Sequence number. If this is provided, Sequence must be 0. Cannot be used with AccountTxnID. | [optional] 
**txn_signature** | **str** | The signature that verifies this transaction as originating from the account it says it is from. | [optional] 

## Example

```python
from openapi_client.models.payment_transaction_base import PaymentTransactionBase

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTransactionBase from a JSON string
payment_transaction_base_instance = PaymentTransactionBase.from_json(json)
# print the JSON string representation of the object
print(PaymentTransactionBase.to_json())

# convert the object into a dict
payment_transaction_base_dict = payment_transaction_base_instance.to_dict()
# create an instance of PaymentTransactionBase from a dict
payment_transaction_base_from_dict = PaymentTransactionBase.from_dict(payment_transaction_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


