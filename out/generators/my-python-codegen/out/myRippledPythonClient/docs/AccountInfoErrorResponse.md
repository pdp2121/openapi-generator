# AccountInfoErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AccountChannelsErrorResponseError**](AccountChannelsErrorResponseError.md) |  | 
**status** | **str** |  | 
**request** | [**AccountInfoRequest**](AccountInfoRequest.md) |  | 

## Example

```python
from openapi_client.models.account_info_error_response import AccountInfoErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoErrorResponse from a JSON string
account_info_error_response_instance = AccountInfoErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AccountInfoErrorResponse.to_json())

# convert the object into a dict
account_info_error_response_dict = account_info_error_response_instance.to_dict()
# create an instance of AccountInfoErrorResponse from a dict
account_info_error_response_from_dict = AccountInfoErrorResponse.from_dict(account_info_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


