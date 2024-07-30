# AccountChannelsResponseResultChannelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_channels_response_result_channels_inner import AccountChannelsResponseResultChannelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountChannelsResponseResultChannelsInner from a JSON string
account_channels_response_result_channels_inner_instance = AccountChannelsResponseResultChannelsInner.from_json(json)
# print the JSON string representation of the object
print(AccountChannelsResponseResultChannelsInner.to_json())

# convert the object into a dict
account_channels_response_result_channels_inner_dict = account_channels_response_result_channels_inner_instance.to_dict()
# create an instance of AccountChannelsResponseResultChannelsInner from a dict
account_channels_response_result_channels_inner_from_dict = AccountChannelsResponseResultChannelsInner.from_dict(account_channels_response_result_channels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


