# SubmitErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**SubmitErrorResponseError**](SubmitErrorResponseError.md) |  | 
**status** | **str** |  | 
**request** | [**SubmitErrorResponseRequest**](SubmitErrorResponseRequest.md) |  | 

## Example

```python
from openapi_client.models.submit_error_response import SubmitErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitErrorResponse from a JSON string
submit_error_response_instance = SubmitErrorResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitErrorResponse.to_json())

# convert the object into a dict
submit_error_response_dict = submit_error_response_instance.to_dict()
# create an instance of SubmitErrorResponse from a dict
submit_error_response_from_dict = SubmitErrorResponse.from_dict(submit_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


