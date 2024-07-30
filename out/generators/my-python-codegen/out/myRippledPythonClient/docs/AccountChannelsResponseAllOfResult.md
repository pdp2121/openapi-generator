# AccountChannelsResponseAllOfResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**channels** | [**List[AccountChannelsResponseAllOfResultChannels]**](AccountChannelsResponseAllOfResultChannels.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_channels_response_all_of_result import AccountChannelsResponseAllOfResult

# TODO update the JSON string below
json = "{}"
# create an instance of AccountChannelsResponseAllOfResult from a JSON string
account_channels_response_all_of_result_instance = AccountChannelsResponseAllOfResult.from_json(json)
# print the JSON string representation of the object
print(AccountChannelsResponseAllOfResult.to_json())

# convert the object into a dict
account_channels_response_all_of_result_dict = account_channels_response_all_of_result_instance.to_dict()
# create an instance of AccountChannelsResponseAllOfResult from a dict
account_channels_response_all_of_result_from_dict = AccountChannelsResponseAllOfResult.from_dict(account_channels_response_all_of_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


