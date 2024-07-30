# SchemasSubmitRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | [**List[SubmitRequestV1]**](SubmitRequestV1.md) |  | [optional] 
**method** | **str** |  | 

## Example

```python
from openapi_client.models.schemas_submit_request_v1 import SchemasSubmitRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasSubmitRequestV1 from a JSON string
schemas_submit_request_v1_instance = SchemasSubmitRequestV1.from_json(json)
# print the JSON string representation of the object
print(SchemasSubmitRequestV1.to_json())

# convert the object into a dict
schemas_submit_request_v1_dict = schemas_submit_request_v1_instance.to_dict()
# create an instance of SchemasSubmitRequestV1 from a dict
schemas_submit_request_v1_from_dict = SchemasSubmitRequestV1.from_dict(schemas_submit_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


