# AccountChannelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AccountChannelsResponseResult**](AccountChannelsResponseResult.md) |  | 

## Example

```python
from openapi_client.models.account_channels_response import AccountChannelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountChannelsResponse from a JSON string
account_channels_response_instance = AccountChannelsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountChannelsResponse.to_json())

# convert the object into a dict
account_channels_response_dict = account_channels_response_instance.to_dict()
# create an instance of AccountChannelsResponse from a dict
account_channels_response_from_dict = AccountChannelsResponse.from_dict(account_channels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


