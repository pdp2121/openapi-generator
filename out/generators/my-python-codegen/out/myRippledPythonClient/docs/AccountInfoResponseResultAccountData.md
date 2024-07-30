# AccountInfoResponseResultAccountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_info_response_result_account_data import AccountInfoResponseResultAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoResponseResultAccountData from a JSON string
account_info_response_result_account_data_instance = AccountInfoResponseResultAccountData.from_json(json)
# print the JSON string representation of the object
print(AccountInfoResponseResultAccountData.to_json())

# convert the object into a dict
account_info_response_result_account_data_dict = account_info_response_result_account_data_instance.to_dict()
# create an instance of AccountInfoResponseResultAccountData from a dict
account_info_response_result_account_data_from_dict = AccountInfoResponseResultAccountData.from_dict(account_info_response_result_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


