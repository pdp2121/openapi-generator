# SignerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | An XRP Ledger address whose signature contributes to the multi-signature. It does not need to be a funded address in the ledger. | [optional] 
**signer_weight** | **float** | The weight of a signature from this signer. A multi-signature is only valid if the sum weight of the signatures provided meets or exceeds the signer list&#39;s SignerQuorum value. | [optional] 
**wallet_locator** | **str** | Arbitrary hexadecimal data. This can be used to identify the signer or for other, related purposes. (Optional) | [optional] 

## Example

```python
from openapi_client.models.signer_entry import SignerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SignerEntry from a JSON string
signer_entry_instance = SignerEntry.from_json(json)
# print the JSON string representation of the object
print(SignerEntry.to_json())

# convert the object into a dict
signer_entry_dict = signer_entry_instance.to_dict()
# create an instance of SignerEntry from a dict
signer_entry_from_dict = SignerEntry.from_dict(signer_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


