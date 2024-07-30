# POSTRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**params** | [**List[SubmitRequestV1]**](SubmitRequestV1.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_request import POSTRequest

# TODO update the JSON string below
json = "{}"
# create an instance of POSTRequest from a JSON string
post_request_instance = POSTRequest.from_json(json)
# print the JSON string representation of the object
print(POSTRequest.to_json())

# convert the object into a dict
post_request_dict = post_request_instance.to_dict()
# create an instance of POSTRequest from a dict
post_request_from_dict = POSTRequest.from_dict(post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


