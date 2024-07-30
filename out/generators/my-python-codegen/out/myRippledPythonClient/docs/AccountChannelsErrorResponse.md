# AccountChannelsErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AccountChannelsErrorResponseError**](AccountChannelsErrorResponseError.md) |  | 
**status** | **str** |  | 
**request** | [**AccountChannelsRequest**](AccountChannelsRequest.md) |  | 

## Example

```python
from openapi_client.models.account_channels_error_response import AccountChannelsErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountChannelsErrorResponse from a JSON string
account_channels_error_response_instance = AccountChannelsErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AccountChannelsErrorResponse.to_json())

# convert the object into a dict
account_channels_error_response_dict = account_channels_error_response_instance.to_dict()
# create an instance of AccountChannelsErrorResponse from a dict
account_channels_error_response_from_dict = AccountChannelsErrorResponse.from_dict(account_channels_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


