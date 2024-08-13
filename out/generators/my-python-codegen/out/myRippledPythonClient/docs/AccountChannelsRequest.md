# AccountChannelsRequest

The account_channels method returns information about an account's Payment Channels.  This includes only channels where the specified account is the channel's source, not the destination.  (A channel's source and owner are the same.) All information retrieved is relative to a particular version of the ledger.  Returns an AccountChannelsResponse. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The unique identifier of an account, typically the account&#39;s address. | 
**destination_account** | **str** | The unique identifier of an account, typically the account&#39;s address. If provided, filter results to payment channels whose destination is this account. | [optional] 
**limit** | **float** | Limit the number of transactions to retrieve. Cannot be less than 10 or more than 400. The default is 200. | [optional] 
**marker** | **object** | Value from a previous paginated response. Resume retrieving data where that response left off. | [optional] 
**ledger_hash** | **str** | A 20-byte hex string for the ledger version to use. | [optional] 
**ledger_index** | [**LookupByLedgerRequestLedgerIndex**](LookupByLedgerRequestLedgerIndex.md) |  | [optional] 
**api_version** | **int** | The API version to use. If omitted, uses version 1. | [optional] 

## Example

```python
from openapi_client.models.account_channels_request import AccountChannelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountChannelsRequest from a JSON string
account_channels_request_instance = AccountChannelsRequest.from_json(json)
# print the JSON string representation of the object
print(AccountChannelsRequest.to_json())

# convert the object into a dict
account_channels_request_dict = account_channels_request_instance.to_dict()
# create an instance of AccountChannelsRequest from a dict
account_channels_request_from_dict = AccountChannelsRequest.from_dict(account_channels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


