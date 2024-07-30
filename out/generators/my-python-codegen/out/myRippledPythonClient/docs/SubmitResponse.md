# SubmitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**result** | [**SubmitResponseAllOfResult**](SubmitResponseAllOfResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.submit_response import SubmitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitResponse from a JSON string
submit_response_instance = SubmitResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitResponse.to_json())

# convert the object into a dict
submit_response_dict = submit_response_instance.to_dict()
# create an instance of SubmitResponse from a dict
submit_response_from_dict = SubmitResponse.from_dict(submit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


