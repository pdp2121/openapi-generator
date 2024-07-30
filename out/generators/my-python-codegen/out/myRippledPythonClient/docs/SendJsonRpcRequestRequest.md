# SendJsonRpcRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**account** | **str** |  | 
**ledger_index** | **str** |  | [optional] 
**tx_blob** | **str** |  | 

## Example

```python
from openapi_client.models.send_json_rpc_request_request import SendJsonRpcRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendJsonRpcRequestRequest from a JSON string
send_json_rpc_request_request_instance = SendJsonRpcRequestRequest.from_json(json)
# print the JSON string representation of the object
print(SendJsonRpcRequestRequest.to_json())

# convert the object into a dict
send_json_rpc_request_request_dict = send_json_rpc_request_request_instance.to_dict()
# create an instance of SendJsonRpcRequestRequest from a dict
send_json_rpc_request_request_from_dict = SendJsonRpcRequestRequest.from_dict(send_json_rpc_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


