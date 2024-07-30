# AccountInfoSuccessResponseBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarded** | **bool** | Indicates whether the request was forwarded. | [optional] 
**status** | **str** | The status of the response (e.g., &#39;success&#39;). | 
**warning** | **str** | A specific warning type (e.g., &#39;load&#39;). | [optional] 
**warnings** | [**List[ResponseWarning]**](ResponseWarning.md) | An array of response warnings. | [optional] 
**account_flags** | [**AccountFlags**](AccountFlags.md) | The account&#39;s flag statuses. | [optional] 
**ledger_current_index** | **int** | The ledger index of the current in-progress ledger. | [optional] 
**ledger_index** | **int** | The ledger index of the ledger version used when retrieving this information. | [optional] 
**queue_data** | [**QueueData**](QueueData.md) | Information about queued transactions sent by this account. | [optional] 
**validated** | **bool** | True if this data is from a validated ledger version; if omitted or set to false, this data is not final. | [optional] 

## Example

```python
from openapi_client.models.account_info_success_response_base import AccountInfoSuccessResponseBase

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoSuccessResponseBase from a JSON string
account_info_success_response_base_instance = AccountInfoSuccessResponseBase.from_json(json)
# print the JSON string representation of the object
print(AccountInfoSuccessResponseBase.to_json())

# convert the object into a dict
account_info_success_response_base_dict = account_info_success_response_base_instance.to_dict()
# create an instance of AccountInfoSuccessResponseBase from a dict
account_info_success_response_base_from_dict = AccountInfoSuccessResponseBase.from_dict(account_info_success_response_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


