# AccountInfoResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AccountInfoResponseV1Result**](AccountInfoResponseV1Result.md) |  | 

## Example

```python
from openapi_client.models.account_info_response_v1 import AccountInfoResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoResponseV1 from a JSON string
account_info_response_v1_instance = AccountInfoResponseV1.from_json(json)
# print the JSON string representation of the object
print(AccountInfoResponseV1.to_json())

# convert the object into a dict
account_info_response_v1_dict = account_info_response_v1_instance.to_dict()
# create an instance of AccountInfoResponseV1 from a dict
account_info_response_v1_from_dict = AccountInfoResponseV1.from_dict(account_info_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


