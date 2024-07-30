# BaseSuccessResponse

Information which is included in every successful response from a request sent to rippled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarded** | **bool** | Indicates whether the request was forwarded. | [optional] 
**status** | **str** | The status of the response (e.g., &#39;success&#39;). | 
**warning** | **str** | A specific warning type (e.g., &#39;load&#39;). | [optional] 
**warnings** | [**List[ResponseWarning]**](ResponseWarning.md) | An array of response warnings. | [optional] 

## Example

```python
from openapi_client.models.base_success_response import BaseSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSuccessResponse from a JSON string
base_success_response_instance = BaseSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(BaseSuccessResponse.to_json())

# convert the object into a dict
base_success_response_dict = base_success_response_instance.to_dict()
# create an instance of BaseSuccessResponse from a dict
base_success_response_from_dict = BaseSuccessResponse.from_dict(base_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


