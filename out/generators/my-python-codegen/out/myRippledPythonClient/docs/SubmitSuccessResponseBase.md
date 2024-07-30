# SubmitSuccessResponseBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarded** | **bool** | Indicates whether the request was forwarded. | [optional] 
**status** | **str** | The status of the response (e.g., &#39;success&#39;). | 
**warning** | **str** | A specific warning type (e.g., &#39;load&#39;). | [optional] 
**warnings** | [**List[ResponseWarning]**](ResponseWarning.md) | An array of response warnings. | [optional] 
**engine_result** | **str** | Text result code indicating the preliminary result of the transaction, for example tesSUCCESS | [optional] 
**engine_result_code** | **int** | Numeric version of the result code. Not recommended. | [optional] 
**engine_result_message** | **str** | Human-readable explanation of the transaction&#39;s preliminary result | [optional] 
**tx_blob** | **str** | The complete transaction in hex string format | [optional] 
**accepted** | **bool** | (Omitted in sign-and-submit mode) The value true indicates that the transaction was applied, queued, broadcast, or kept for later. The value false indicates that none of those happened, so the transaction cannot possibly succeed as long as you do not submit it again and have not already submitted it another time.  | [optional] 
**account_sequence_available** | **float** | (Omitted in sign-and-submit mode) The next Sequence Number available for the sending account after all pending and queued transactions.  | [optional] 
**account_sequence_next** | **float** | (Omitted in sign-and-submit mode) The next Sequence Number for the sending account after all transactions that have been provisionally applied, but not transactions in the queue.  | [optional] 
**applied** | **bool** | (Omitted in sign-and-submit mode) The value true indicates that this transaction was applied to the open ledger. In this case, the transaction is likely, but not guaranteed, to be validated in the next ledger version.  | [optional] 
**broadcast** | **bool** | (Omitted in sign-and-submit mode) The value true indicates this transaction was broadcast to peer servers in the peer-to-peer XRP Ledger network. (Note: if the server has no peers, such as in stand-alone mode, the server uses the value true for cases where it would have broadcast the transaction.) The value false indicates the transaction was not broadcast to any other servers.  | [optional] 
**kept** | **bool** | (Omitted in sign-and-submit mode) The value true indicates that the transaction was kept to be retried later.  | [optional] 
**queued** | **bool** | (Omitted in sign-and-submit mode) The value true indicates the transaction was put in the Transaction Queue, which means it is likely to be included in a future ledger version.  | [optional] 
**open_ledger_cost** | **str** | (Omitted in sign-and-submit mode) The current open ledger cost before processing this transaction. Transactions with a lower cost are likely to be queued.  | [optional] 
**validated_ledger_index** | **int** | (Omitted in sign-and-submit mode) The ledger index of the newest validated ledger at the time of submission. This provides a lower bound on the ledger versions that the transaction can appear in as a result of this request. (The transaction could only have been validated in this ledger version or earlier if it had already been submitted before.)  | [optional] 

## Example

```python
from openapi_client.models.submit_success_response_base import SubmitSuccessResponseBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitSuccessResponseBase from a JSON string
submit_success_response_base_instance = SubmitSuccessResponseBase.from_json(json)
# print the JSON string representation of the object
print(SubmitSuccessResponseBase.to_json())

# convert the object into a dict
submit_success_response_base_dict = submit_success_response_base_instance.to_dict()
# create an instance of SubmitSuccessResponseBase from a dict
submit_success_response_base_from_dict = SubmitSuccessResponseBase.from_dict(submit_success_response_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


