# Channel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The owner of the channel, as an Address. | 
**amount** | **str** | The total amount of XRP, in drops allocated to this channel. | 
**balance** | **str** | The total amount of XRP, in drops, paid out from this channel, as of the ledger version used. (You can calculate the amount of XRP left in the channel by subtracting balance from amount.)  | 
**cancel_after** | **int** | Time, in seconds since the Ripple Epoch, of this channel&#39;s immutable expiration, if one was specified at channel creation. If this is before the close time of the most recent validated ledger, the channel is expired.  | [optional] 
**channel_id** | **str** | A unique ID for this channel, as a 64-character hexadecimal string. This is also the ID of the channel object in the ledger&#39;s state data.  | 
**destination_account** | **str** | The destination account of the channel, as an Address. Only this account can receive the XRP in the channel while it is open. | 
**destination_tag** | **int** | A 32-bit unsigned integer to use as a destination tag for payments through this channel, if one was specified at channel creation. This indicates the payment channel&#39;s beneficiary or other purpose at the destination account.  | [optional] 
**expiration** | **int** | Time, in seconds since the Ripple Epoch, when this channel is set to expire. This expiration date is mutable. If this is before the close time of the most recent validated ledger, the channel is expired.  | [optional] 
**public_key** | **str** | The public key for the payment channel in the XRP Ledger&#39;s base58 format. Signed claims against this channel must be redeemed with the matching key pair.  | [optional] 
**public_key_hex** | **str** | The public key for the payment channel in hexadecimal format, if one was specified at channel creation. Signed claims against this channel must be redeemed with the matching key pair.  | [optional] 
**settle_delay** | **int** | The number of seconds the payment channel must stay open after the owner of the channel requests to close it.  | 
**source_tag** | **int** | A 32-bit unsigned integer to use as a source tag for payments through this payment channel, if one was specified at channel creation. This indicates the payment channel&#39;s originator or other purpose at the source account.  | [optional] 

## Example

```python
from openapi_client.models.channel import Channel

# TODO update the JSON string below
json = "{}"
# create an instance of Channel from a JSON string
channel_instance = Channel.from_json(json)
# print the JSON string representation of the object
print(Channel.to_json())

# convert the object into a dict
channel_dict = channel_instance.to_dict()
# create an instance of Channel from a dict
channel_from_dict = Channel.from_dict(channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


