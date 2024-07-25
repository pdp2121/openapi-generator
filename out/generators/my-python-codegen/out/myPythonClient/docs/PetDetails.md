# PetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**breed** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pet_details import PetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PetDetails from a JSON string
pet_details_instance = PetDetails.from_json(json)
# print the JSON string representation of the object
print(PetDetails.to_json())

# convert the object into a dict
pet_details_dict = pet_details_instance.to_dict()
# create an instance of PetDetails from a dict
pet_details_from_dict = PetDetails.from_dict(pet_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


