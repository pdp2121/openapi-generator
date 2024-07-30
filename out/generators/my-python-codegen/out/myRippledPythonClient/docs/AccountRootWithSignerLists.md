# AccountRootWithSignerLists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The identifying (classic) address of this account. | 
**account_txn_id** | **str** | The identifying hash of the transaction most recently sent by this account. (Optional) | [optional] 
**ammid** | **str** | The ledger entry ID of the corresponding AMM ledger entry. (Optional) | [optional] 
**balance** | **str** | The account&#39;s current XRP balance in drops, represented as a string. (Optional) | [optional] 
**burned_nf_tokens** | **float** | How many total of this account&#39;s issued non-fungible tokens have been burned. (Optional) | [optional] 
**domain** | **str** | A domain associated with this account. Cannot be more than 256 bytes in length. (Optional) | [optional] 
**email_hash** | **str** | The md5 hash of an email address. Clients can use this to look up an avatar. (Optional) | [optional] 
**first_nf_token_sequence** | **float** | The account&#39;s Sequence Number at the time it minted its first non-fungible-token. (Optional) | [optional] 
**ledger_entry_type** | **str** | The value 0x0061, mapped to the string AccountRoot, indicates that this is an AccountRoot object. | 
**message_key** | **str** | A public key that may be used to send encrypted messages to this account. Must be exactly 33 bytes. (Optional) | [optional] 
**minted_nf_tokens** | **float** | How many total non-fungible tokens have been minted by and on behalf of this account. (Optional) | [optional] 
**nf_token_minter** | **str** | Another account that can mint non-fungible tokens on behalf of this account. (Optional) | [optional] 
**owner_count** | **float** | The number of objects this account owns in the ledger, which contributes to its owner reserve. | 
**previous_txn_id** | **str** | The identifying hash of the transaction that most recently modified this object. | 
**previous_txn_lgr_seq** | **float** | The index of the ledger that contains the transaction that most recently modified this object. | 
**regular_key** | **str** | The address of a key pair that can be used to sign transactions for this account instead of the master key. (Optional) | [optional] 
**sequence** | **float** | The sequence number of the next valid transaction for this account. | 
**ticket_count** | **float** | How many Tickets this account owns in the ledger. (Optional) | [optional] 
**tick_size** | **float** | How many significant digits to use for exchange rates of Offers involving currencies issued by this address. (Optional) | [optional] 
**transfer_rate** | **float** | A transfer fee to charge other users for sending currency issued by this account to each other. (Optional) | [optional] 
**wallet_locator** | **str** | An arbitrary 256-bit value that users can set. (Optional) | [optional] 
**wallet_size** | **float** | Unused. (The code supports this field but there is no way to set it.) (Optional) | [optional] 
**signer_lists** | [**List[SignerList]**](SignerList.md) | Array of SignerList ledger objects associated with this account for Multi-Signing. | [optional] 

## Example

```python
from openapi_client.models.account_root_with_signer_lists import AccountRootWithSignerLists

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRootWithSignerLists from a JSON string
account_root_with_signer_lists_instance = AccountRootWithSignerLists.from_json(json)
# print the JSON string representation of the object
print(AccountRootWithSignerLists.to_json())

# convert the object into a dict
account_root_with_signer_lists_dict = account_root_with_signer_lists_instance.to_dict()
# create an instance of AccountRootWithSignerLists from a dict
account_root_with_signer_lists_from_dict = AccountRootWithSignerLists.from_dict(account_root_with_signer_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


