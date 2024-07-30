# SignerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ledger_entry_type** | **str** | The value 0x0053, mapped to the string SignerList, indicates that this is a SignerList ledger entry. | 
**owner_node** | **str** | A hint indicating which page of the owner directory links to this object, in case the directory consists of multiple pages. | 
**previous_txn_id** | **str** | The identifying hash of the transaction that most recently modified this object. | 
**previous_txn_lgr_seq** | **int** | The index of the ledger that contains the transaction that most recently modified this object. | 
**signer_entries** | [**List[SignerEntry]**](SignerEntry.md) | An array of Signer Entry objects representing the parties who are part of this signer list. | 
**signer_list_id** | **int** | An ID for this signer list. Currently always set to 0. If a future amendment allows multiple signer lists for an account, this may change. | 
**signer_quorum** | **int** | A target number for signer weights. To produce a valid signature for the owner of this SignerList, the signers must provide valid signatures whose weights sum to this value or more. | 

## Example

```python
from openapi_client.models.signer_list import SignerList

# TODO update the JSON string below
json = "{}"
# create an instance of SignerList from a JSON string
signer_list_instance = SignerList.from_json(json)
# print the JSON string representation of the object
print(SignerList.to_json())

# convert the object into a dict
signer_list_dict = signer_list_instance.to_dict()
# create an instance of SignerList from a dict
signer_list_from_dict = SignerList.from_dict(signer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


