# AccountFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_ripple** | **bool** | If true, the account allows rippling on its trust lines by default. | [optional] 
**deposit_auth** | **bool** | If true, the account is using Deposit Authorization and does not accept any payments from unknown parties. | [optional] 
**disable_master_key** | **bool** | If true, the account&#39;s master key pair is disabled. | [optional] 
**disallow_incoming_check** | **bool** | If true, the account does not allow others to send Checks to it. | [optional] 
**disallow_incoming_nf_token_offer** | **bool** | If true, the account does not allow others to make NFT buy or sell offers to it. | [optional] 
**disallow_incoming_pay_chan** | **bool** | If true, the account does not allow others to make Payment Channels to it. | [optional] 
**disallow_incoming_trustline** | **bool** | If true, the account does not allow others to make trust lines to it. | [optional] 
**disallow_incoming_xrp** | **bool** | If true, the account does not want to receive XRP from others. This is advisory and not enforced at a protocol level. | [optional] 
**global_freeze** | **bool** | If true, all tokens issued by the account are currently frozen. | [optional] 
**no_freeze** | **bool** | If true, the account has permanently given up the abilities to freeze individual trust lines or end a global freeze. | [optional] 
**password_spent** | **bool** | If false, the account can send a special key reset transaction with a transaction cost of 0. | [optional] 
**require_authorization** | **bool** | If true, the account is using Authorized Trust Lines to limit who can hold the tokens it issues. | [optional] 
**require_destination_tag** | **bool** | If true, the account requires a destination tag on all payments it receives. | [optional] 

## Example

```python
from openapi_client.models.account_flags import AccountFlags

# TODO update the JSON string below
json = "{}"
# create an instance of AccountFlags from a JSON string
account_flags_instance = AccountFlags.from_json(json)
# print the JSON string representation of the object
print(AccountFlags.to_json())

# convert the object into a dict
account_flags_dict = account_flags_instance.to_dict()
# create an instance of AccountFlags from a dict
account_flags_from_dict = AccountFlags.from_dict(account_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


