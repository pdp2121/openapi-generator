# SubmitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**tx_blob** | **str** |  | 

## Example

```python
from openapi_client.models.submit_request import SubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitRequest from a JSON string
submit_request_instance = SubmitRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitRequest.to_json())

# convert the object into a dict
submit_request_dict = submit_request_instance.to_dict()
# create an instance of SubmitRequest from a dict
submit_request_from_dict = SubmitRequest.from_dict(submit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


