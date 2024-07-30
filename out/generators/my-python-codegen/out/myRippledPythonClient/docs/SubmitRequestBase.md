# SubmitRequestBase

The submit method applies a transaction and sends it to the network to be confirmed and included in future ledgers. This command has two modes: - Submit-only mode takes a signed, serialized transaction as a binary blob, and submits it to the network as-is. Since signed transaction objects are immutable, no part of the transaction can be modified or automatically filled in after submission. - Sign-and-submit mode takes a JSON-formatted Transaction object, completes and signs the transaction in the same manner as the sign method, and then submits the signed transaction. We recommend only using this mode for testing and development. To send a transaction as robustly as possible, you should construct and sign it in advance, persist it somewhere that you can access even after a power outage, then submit it as a tx_blob. After submission, monitor the network with the tx method command to see if the transaction was successfully applied; if a restart or other problem occurs, you can safely re-submit the tx_blob transaction: it won't be applied twice since it has the same sequence number as the old transaction. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 

## Example

```python
from openapi_client.models.submit_request_base import SubmitRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitRequestBase from a JSON string
submit_request_base_instance = SubmitRequestBase.from_json(json)
# print the JSON string representation of the object
print(SubmitRequestBase.to_json())

# convert the object into a dict
submit_request_base_dict = submit_request_base_instance.to_dict()
# create an instance of SubmitRequestBase from a dict
submit_request_base_from_dict = SubmitRequestBase.from_dict(submit_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


