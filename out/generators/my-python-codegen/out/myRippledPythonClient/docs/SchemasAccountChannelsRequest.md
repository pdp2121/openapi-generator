# SchemasAccountChannelsRequest

The account_channels method returns information about an account's Payment Channels.  This includes only channels where the specified account is the channel's source, not the destination.  (A channel's source and owner are the same.) All information retrieved is relative to a particular version of the ledger.  Returns an AccountChannelsResponse. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**params** | [**List[AccountChannelsRequest]**](AccountChannelsRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.schemas_account_channels_request import SchemasAccountChannelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasAccountChannelsRequest from a JSON string
schemas_account_channels_request_instance = SchemasAccountChannelsRequest.from_json(json)
# print the JSON string representation of the object
print(SchemasAccountChannelsRequest.to_json())

# convert the object into a dict
schemas_account_channels_request_dict = schemas_account_channels_request_instance.to_dict()
# create an instance of SchemasAccountChannelsRequest from a dict
schemas_account_channels_request_from_dict = SchemasAccountChannelsRequest.from_dict(schemas_account_channels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


