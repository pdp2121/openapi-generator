# LookupByLedgerRequest

Additional information shared in requests which search for specific ledger data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ledger_hash** | **str** | A 20-byte hex string for the ledger version to use. | [optional] 
**ledger_index** | [**LookupByLedgerRequestLedgerIndex**](LookupByLedgerRequestLedgerIndex.md) |  | [optional] 

## Example

```python
from openapi_client.models.lookup_by_ledger_request import LookupByLedgerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LookupByLedgerRequest from a JSON string
lookup_by_ledger_request_instance = LookupByLedgerRequest.from_json(json)
# print the JSON string representation of the object
print(LookupByLedgerRequest.to_json())

# convert the object into a dict
lookup_by_ledger_request_dict = lookup_by_ledger_request_instance.to_dict()
# create an instance of LookupByLedgerRequest from a dict
lookup_by_ledger_request_from_dict = LookupByLedgerRequest.from_dict(lookup_by_ledger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


