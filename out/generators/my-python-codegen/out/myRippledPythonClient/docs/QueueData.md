# QueueData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_count** | **int** | Number of queued transactions from this address. | [optional] 
**auth_change_queued** | **bool** | Whether a transaction in the queue changes this address&#39;s ways of authorizing transactions. | [optional] 
**lowest_sequence** | **int** | The lowest Sequence Number among transactions queued by this address. | [optional] 
**highest_sequence** | **int** | The highest Sequence Number among transactions queued by this address. | [optional] 
**max_spend_drops_total** | **str** | Integer amount of drops of XRP that could be debited from this address if every transaction in the queue consumes the maximum amount of XRP possible. | [optional] 
**transactions** | [**List[Transactions]**](Transactions.md) | Information about each queued transaction from this address. | [optional] 

## Example

```python
from openapi_client.models.queue_data import QueueData

# TODO update the JSON string below
json = "{}"
# create an instance of QueueData from a JSON string
queue_data_instance = QueueData.from_json(json)
# print the JSON string representation of the object
print(QueueData.to_json())

# convert the object into a dict
queue_data_dict = queue_data_instance.to_dict()
# create an instance of QueueData from a dict
queue_data_from_dict = QueueData.from_dict(queue_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


