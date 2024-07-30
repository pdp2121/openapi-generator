# SendJsonRpcRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**result** | [**SubmitResponseAllOfResult**](SubmitResponseAllOfResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.send_json_rpc_request200_response import SendJsonRpcRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendJsonRpcRequest200Response from a JSON string
send_json_rpc_request200_response_instance = SendJsonRpcRequest200Response.from_json(json)
# print the JSON string representation of the object
print(SendJsonRpcRequest200Response.to_json())

# convert the object into a dict
send_json_rpc_request200_response_dict = send_json_rpc_request200_response_instance.to_dict()
# create an instance of SendJsonRpcRequest200Response from a dict
send_json_rpc_request200_response_from_dict = SendJsonRpcRequest200Response.from_dict(send_json_rpc_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


