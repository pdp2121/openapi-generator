# SubmitResponseAllOfResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine_result** | **str** |  | [optional] 
**tx_json** | [**SubmitResponseAllOfResultTxJson**](SubmitResponseAllOfResultTxJson.md) |  | [optional] 

## Example

```python
from openapi_client.models.submit_response_all_of_result import SubmitResponseAllOfResult

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitResponseAllOfResult from a JSON string
submit_response_all_of_result_instance = SubmitResponseAllOfResult.from_json(json)
# print the JSON string representation of the object
print(SubmitResponseAllOfResult.to_json())

# convert the object into a dict
submit_response_all_of_result_dict = submit_response_all_of_result_instance.to_dict()
# create an instance of SubmitResponseAllOfResult from a dict
submit_response_all_of_result_from_dict = SubmitResponseAllOfResult.from_dict(submit_response_all_of_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


