# ResponseWarning

Used to share rate-limiting warnings or other potential issues with a request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **Dict[str, str]** | Additional information about this warning. The contents vary depending on the type of warning. | [optional] 
**id** | **int** | A unique numeric code for this warning message. | 
**message** | **str** | A human-readable string describing the cause of this message. Do not write software that relies the contents of this message; use the id (and details, if applicable) to identify the warning instead.  | 

## Example

```python
from openapi_client.models.response_warning import ResponseWarning

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseWarning from a JSON string
response_warning_instance = ResponseWarning.from_json(json)
# print the JSON string representation of the object
print(ResponseWarning.to_json())

# convert the object into a dict
response_warning_dict = response_warning_instance.to_dict()
# create an instance of ResponseWarning from a dict
response_warning_from_dict = ResponseWarning.from_dict(response_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


