# SchemasAccountInfoRequest

The account_info command retrieves information about an account, its activity, and its XRP balance. All information retrieved is relative to a particular version of the ledger. Returns an AccountInfoResponse 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**params** | [**List[AccountInfoRequest]**](AccountInfoRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.schemas_account_info_request import SchemasAccountInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasAccountInfoRequest from a JSON string
schemas_account_info_request_instance = SchemasAccountInfoRequest.from_json(json)
# print the JSON string representation of the object
print(SchemasAccountInfoRequest.to_json())

# convert the object into a dict
schemas_account_info_request_dict = schemas_account_info_request_instance.to_dict()
# create an instance of SchemasAccountInfoRequest from a dict
schemas_account_info_request_from_dict = SchemasAccountInfoRequest.from_dict(schemas_account_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


