# SubmitOnlyMode

A submit-only request for submitting transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_blob** | **str** | Hex representation of the signed transaction to submit. Can be a multi-signed transaction. | 
**fail_hard** | **bool** | If true, and the transaction fails locally, do not retry or relay the transaction to other servers. Default is false. | [optional] 

## Example

```python
from openapi_client.models.submit_only_mode import SubmitOnlyMode

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitOnlyMode from a JSON string
submit_only_mode_instance = SubmitOnlyMode.from_json(json)
# print the JSON string representation of the object
print(SubmitOnlyMode.to_json())

# convert the object into a dict
submit_only_mode_dict = submit_only_mode_instance.to_dict()
# create an instance of SubmitOnlyMode from a dict
submit_only_mode_from_dict = SubmitOnlyMode.from_dict(submit_only_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


