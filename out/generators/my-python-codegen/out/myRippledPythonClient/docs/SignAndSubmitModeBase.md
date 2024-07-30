# SignAndSubmitModeBase

A mode for signing a transaction and immediately submitting it. This mode is intended for testing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | (Optional) Secret key of the account supplying the transaction, used to sign it. Do not send your secret to untrusted servers or through unsecured network connections. Cannot be used with key_type, seed, seed_hex, or passphrase. | [optional] 
**seed** | **str** | (Optional) Secret key of the account supplying the transaction, used to sign it. Must be in the XRP Ledger&#39;s base58 format. If provided, you must also specify the key_type. Cannot be used with secret, seed_hex, or passphrase. | [optional] 
**seed_hex** | **str** | (Optional) Secret key of the account supplying the transaction, used to sign it. Must be in hexadecimal format. If provided, you must also specify the key_type. Cannot be used with secret, seed, or passphrase. | [optional] 
**passphrase** | **str** | (Optional) Secret key of the account supplying the transaction, used to sign it, as a string passphrase. If provided, you must also specify the key_type. Cannot be used with secret, seed, or seed_hex. | [optional] 
**key_type** | **str** | (Optional) Type of cryptographic key provided in this request. Valid types are secp256k1 or ed25519. Defaults to secp256k1. Cannot be used with secret. Caution: Ed25519 support is experimental. | [optional] 
**fail_hard** | **bool** | (Optional) If true, and the transaction fails locally, do not retry or relay the transaction to other servers. Default is false. Updated in: rippled 1.5.0 | [optional] 
**offline** | **bool** | (Optional) If true, when constructing the transaction, do not try to automatically fill in or validate values. Default is false. | [optional] 
**build_path** | **bool** | (Optional) If this field is provided, the server auto-fills the Paths field of a Payment transaction before signing. Omit this field if the transaction is a direct XRP payment or if it is not a Payment-type transaction. Caution: The server looks for the presence or absence of this field, not its value. This behavior may change. (Issue #3272) | [optional] 
**fee_mult_max** | **int** | (Optional) Sign-and-submit fails with the error rpcHIGH_FEE if the auto-filled Fee value would be greater than the reference transaction cost x fee_mult_max ÷ fee_div_max. This field has no effect if you explicitly specify the Fee field of the transaction. Default is 10. | [optional] 
**fee_div_max** | **int** | (Optional) Sign-and-submit fails with the error rpcHIGH_FEE if the auto-filled Fee value would be greater than the reference transaction cost x fee_mult_max ÷ fee_div_max. This field has no effect if you explicitly specify the Fee field of the transaction. Default is 1. | [optional] 

## Example

```python
from openapi_client.models.sign_and_submit_mode_base import SignAndSubmitModeBase

# TODO update the JSON string below
json = "{}"
# create an instance of SignAndSubmitModeBase from a JSON string
sign_and_submit_mode_base_instance = SignAndSubmitModeBase.from_json(json)
# print the JSON string representation of the object
print(SignAndSubmitModeBase.to_json())

# convert the object into a dict
sign_and_submit_mode_base_dict = sign_and_submit_mode_base_instance.to_dict()
# create an instance of SignAndSubmitModeBase from a dict
sign_and_submit_mode_base_from_dict = SignAndSubmitModeBase.from_dict(sign_and_submit_mode_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


