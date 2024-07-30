# Transactions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_change** | **bool** | Whether this transaction changes this address&#39;s ways of authorizing transactions. | [optional] 
**fee** | **str** | The Transaction Cost of this transaction, in drops of XRP. | [optional] 
**fee_level** | **str** | The transaction cost of this transaction, relative to the minimum cost for this type of transaction, in fee levels. | [optional] 
**max_spend_drops** | **str** | The maximum amount of XRP, in drops, this transaction could send or destroy. | [optional] 
**seq** | **int** | The Sequence Number of this transaction. | [optional] 

## Example

```python
from openapi_client.models.transactions import Transactions

# TODO update the JSON string below
json = "{}"
# create an instance of Transactions from a JSON string
transactions_instance = Transactions.from_json(json)
# print the JSON string representation of the object
print(Transactions.to_json())

# convert the object into a dict
transactions_dict = transactions_instance.to_dict()
# create an instance of Transactions from a dict
transactions_from_dict = Transactions.from_dict(transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


