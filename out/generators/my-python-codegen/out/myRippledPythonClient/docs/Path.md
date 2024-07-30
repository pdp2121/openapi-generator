# Path


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | (Optional) If present, this path step represents rippling through the specified address. MUST NOT be provided if this step specifies the currency or issuer fields. | [optional] 
**currency** | **str** | (Optional) If present, this path step represents changing currencies through an order book. The currency specified indicates the new currency. MUST NOT be provided if this step specifies the account field. | [optional] 
**issuer** | **str** | (Optional) If present, this path step represents changing currencies and this address defines the issuer of the new currency. If omitted in a step with a non-XRP currency, a previous step of the path defines the issuer. If present when currency is omitted, indicates a path step that uses an order book between same-named currencies with different issuers. MUST be omitted if the currency is XRP. MUST NOT be provided if this step specifies the account field. | [optional] 
**type** | **int** | DEPRECATED (Optional) An indicator of which other fields are present. | [optional] 
**type_hex** | **str** | DEPRECATED: (Optional) A hexadecimal representation of the type field. | [optional] 

## Example

```python
from openapi_client.models.path import Path

# TODO update the JSON string below
json = "{}"
# create an instance of Path from a JSON string
path_instance = Path.from_json(json)
# print the JSON string representation of the object
print(Path.to_json())

# convert the object into a dict
path_dict = path_instance.to_dict()
# create an instance of Path from a dict
path_from_dict = Path.from_dict(path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


