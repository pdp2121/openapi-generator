# BaseTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The unique address of the account that initiated the transaction. | 
**transaction_type** | **str** | The type of transaction. Valid transaction types include: Payment, OfferCreate, TrustSet, and many others.  | 
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
from openapi_client.models.base_transaction import BaseTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTransaction from a JSON string
base_transaction_instance = BaseTransaction.from_json(json)
# print the JSON string representation of the object
print(BaseTransaction.to_json())

# convert the object into a dict
base_transaction_dict = base_transaction_instance.to_dict()
# create an instance of BaseTransaction from a dict
base_transaction_from_dict = BaseTransaction.from_dict(base_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


