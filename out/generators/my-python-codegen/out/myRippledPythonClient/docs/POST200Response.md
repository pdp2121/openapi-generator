# POST200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SubmitResponseV1Result**](SubmitResponseV1Result.md) |  | 

## Example

```python
from openapi_client.models.post200_response import POST200Response

# TODO update the JSON string below
json = "{}"
# create an instance of POST200Response from a JSON string
post200_response_instance = POST200Response.from_json(json)
# print the JSON string representation of the object
print(POST200Response.to_json())

# convert the object into a dict
post200_response_dict = post200_response_instance.to_dict()
# create an instance of POST200Response from a dict
post200_response_from_dict = POST200Response.from_dict(post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


