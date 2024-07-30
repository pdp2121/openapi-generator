# BaseRequest

Information which could be included in every request sent to rippled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **int** | The API version to use. If omitted, uses version 1. | [optional] 

## Example

```python
from openapi_client.models.base_request import BaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRequest from a JSON string
base_request_instance = BaseRequest.from_json(json)
# print the JSON string representation of the object
print(BaseRequest.to_json())

# convert the object into a dict
base_request_dict = base_request_instance.to_dict()
# create an instance of BaseRequest from a dict
base_request_from_dict = BaseRequest.from_dict(base_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


