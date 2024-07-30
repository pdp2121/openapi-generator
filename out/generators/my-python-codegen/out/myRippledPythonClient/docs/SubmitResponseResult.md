# SubmitResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine_result** | **str** |  | [optional] 
**tx_json** | [**SubmitResponseResultTxJson**](SubmitResponseResultTxJson.md) |  | [optional] 

## Example

```python
from openapi_client.models.submit_response_result import SubmitResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitResponseResult from a JSON string
submit_response_result_instance = SubmitResponseResult.from_json(json)
# print the JSON string representation of the object
print(SubmitResponseResult.to_json())

# convert the object into a dict
submit_response_result_dict = submit_response_result_instance.to_dict()
# create an instance of SubmitResponseResult from a dict
submit_response_result_from_dict = SubmitResponseResult.from_dict(submit_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


