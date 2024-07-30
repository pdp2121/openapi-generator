# SubmitResponseResultTxJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | [optional] 
**ledger_index** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.submit_response_result_tx_json import SubmitResponseResultTxJson

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitResponseResultTxJson from a JSON string
submit_response_result_tx_json_instance = SubmitResponseResultTxJson.from_json(json)
# print the JSON string representation of the object
print(SubmitResponseResultTxJson.to_json())

# convert the object into a dict
submit_response_result_tx_json_dict = submit_response_result_tx_json_instance.to_dict()
# create an instance of SubmitResponseResultTxJson from a dict
submit_response_result_tx_json_from_dict = SubmitResponseResultTxJson.from_dict(submit_response_result_tx_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


