# AccountInfoResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_data** | [**AccountInfoResponseResultAccountData**](AccountInfoResponseResultAccountData.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_info_response_result import AccountInfoResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoResponseResult from a JSON string
account_info_response_result_instance = AccountInfoResponseResult.from_json(json)
# print the JSON string representation of the object
print(AccountInfoResponseResult.to_json())

# convert the object into a dict
account_info_response_result_dict = account_info_response_result_instance.to_dict()
# create an instance of AccountInfoResponseResult from a dict
account_info_response_result_from_dict = AccountInfoResponseResult.from_dict(account_info_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


