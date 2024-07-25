# BasePet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.base_pet import BasePet

# TODO update the JSON string below
json = "{}"
# create an instance of BasePet from a JSON string
base_pet_instance = BasePet.from_json(json)
# print the JSON string representation of the object
print(BasePet.to_json())

# convert the object into a dict
base_pet_dict = base_pet_instance.to_dict()
# create an instance of BasePet from a dict
base_pet_from_dict = BasePet.from_dict(base_pet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


