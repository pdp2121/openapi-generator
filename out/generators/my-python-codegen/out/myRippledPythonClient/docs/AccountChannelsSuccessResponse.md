# AccountChannelsSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The address of the source/owner of the payment channels. This corresponds to the account field of the request. | 
**channels** | [**List[Channel]**](Channel.md) | Payment channels owned by this account. | [optional] 
**validated** | **bool** | If true, the information in this response comes from a validated ledger version. Otherwise, the information is subject to change. | [optional] 
**limit** | **float** | The limit to how many channel objects were actually returned by this request. | [optional] 
**marker** | **object** | Server-defined value for pagination. Pass this to the next call to resume getting results where this call left off. Omitted when there are no additional pages after this one. | [optional] 
**forwarded** | **bool** | Indicates whether the request was forwarded. | [optional] 
**status** | **str** | The status of the response (e.g., &#39;success&#39;). | 
**warning** | **str** | A specific warning type (e.g., &#39;load&#39;). | [optional] 
**warnings** | [**List[ResponseWarning]**](ResponseWarning.md) | An array of response warnings. | [optional] 
**ledger_hash** | **str** | A 20-byte hex string for the ledger version to use. | [optional] 
**ledger_index** | [**LookupByLedgerRequestLedgerIndex**](LookupByLedgerRequestLedgerIndex.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_channels_success_response import AccountChannelsSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountChannelsSuccessResponse from a JSON string
account_channels_success_response_instance = AccountChannelsSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(AccountChannelsSuccessResponse.to_json())

# convert the object into a dict
account_channels_success_response_dict = account_channels_success_response_instance.to_dict()
# create an instance of AccountChannelsSuccessResponse from a dict
account_channels_success_response_from_dict = AccountChannelsSuccessResponse.from_dict(account_channels_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


