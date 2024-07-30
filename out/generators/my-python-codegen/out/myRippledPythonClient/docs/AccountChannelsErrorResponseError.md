# AccountChannelsErrorResponseError

* `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing. * `actNotFound` - The address specified in the `account` field of the request does not correspond to an account in the ledger. * `lgrNotFound` - The ledger specified by the `ledger_hash` or `ledger_index` does not exist, or it does exist but the server does not have it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.account_channels_error_response_error import AccountChannelsErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of AccountChannelsErrorResponseError from a JSON string
account_channels_error_response_error_instance = AccountChannelsErrorResponseError.from_json(json)
# print the JSON string representation of the object
print(AccountChannelsErrorResponseError.to_json())

# convert the object into a dict
account_channels_error_response_error_dict = account_channels_error_response_error_instance.to_dict()
# create an instance of AccountChannelsErrorResponseError from a dict
account_channels_error_response_error_from_dict = AccountChannelsErrorResponseError.from_dict(account_channels_error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


