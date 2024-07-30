# AccountInfoResponseAllOfResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_data** | [**AccountInfoResponseAllOfResultAccountData**](AccountInfoResponseAllOfResultAccountData.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_info_response_all_of_result import AccountInfoResponseAllOfResult

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoResponseAllOfResult from a JSON string
account_info_response_all_of_result_instance = AccountInfoResponseAllOfResult.from_json(json)
# print the JSON string representation of the object
print(AccountInfoResponseAllOfResult.to_json())

# convert the object into a dict
account_info_response_all_of_result_dict = account_info_response_all_of_result_instance.to_dict()
# create an instance of AccountInfoResponseAllOfResult from a dict
account_info_response_all_of_result_from_dict = AccountInfoResponseAllOfResult.from_dict(account_info_response_all_of_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


