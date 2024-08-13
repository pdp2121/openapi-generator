# AccountInfoRequest

The account_info command retrieves information about an account, its activity, and its XRP balance. All information retrieved is relative to a particular version of the ledger. Returns an AccountInfoResponse 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**account** | **str** | The account to look up. | 
**queue** | **bool** | If true, return stats about queued transactions sent by this account. Can only be used when querying for the data from the current open ledger. Not available from servers in Reporting Mode. | [optional] 
**signer_lists** | **bool** | API v1: If true, return any SignerList objects associated with this account. API v2: Identical to v1, but also returns an invalidParams error if you provide a non-boolean value.  | [optional] 
**ledger_hash** | **str** | A 20-byte hex string for the ledger version to use. | [optional] 
**ledger_index** | [**LookupByLedgerRequestLedgerIndex**](LookupByLedgerRequestLedgerIndex.md) |  | [optional] 
**api_version** | **int** | The API version to use. If omitted, uses version 1. | [optional] 

## Example

```python
from openapi_client.models.account_info_request import AccountInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoRequest from a JSON string
account_info_request_instance = AccountInfoRequest.from_json(json)
# print the JSON string representation of the object
print(AccountInfoRequest.to_json())

# convert the object into a dict
account_info_request_dict = account_info_request_instance.to_dict()
# create an instance of AccountInfoRequest from a dict
account_info_request_from_dict = AccountInfoRequest.from_dict(account_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


