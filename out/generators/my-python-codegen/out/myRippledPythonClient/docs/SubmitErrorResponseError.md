# SubmitErrorResponseError

* `amendmentBlocked` - The transaction cannot be submitted to the network because the rippled server is amendment blocked. * `highFee` - The fee_mult_max parameter was specified, but the server's current fee multiplier exceeds the specified one. (Sign-and-Submit mode only) * `internalJson` - An internal error occurred when serializing the transaction to JSON. This could be caused by many aspects of the transaction, including a bad signature or some fields being malformed. * `internalSubmit` - An internal error occurred when submitting the transaction. This could be caused by many aspects of the transaction, including a bad signature or some fields being malformed. * `internalTransaction` - An internal error occurred when processing the transaction. This could be caused by many aspects of the transaction, including a bad signature or some fields being malformed. * `invalidParams` - One or more fields are specified incorrectly, or one or more required fields are missing. * `invalidTransaction` - The transaction is malformed or otherwise invalid. * `noPath` - The transaction did not include paths, and the server was unable to find a path by which this payment can occur. (Sign-and-Submit mode only) * `tooBusy` - The transaction did not include paths, but the server is too busy to do pathfinding right now. Does not occur if you are connected as an admin. (Sign-and-Submit mode only) * `notSupported` - Signing is not supported by this server (Sign-and-Submit mode only.) If you are the server admin, you can still access signing when connected as an admin, or you could enable public signing. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.submit_error_response_error import SubmitErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitErrorResponseError from a JSON string
submit_error_response_error_instance = SubmitErrorResponseError.from_json(json)
# print the JSON string representation of the object
print(SubmitErrorResponseError.to_json())

# convert the object into a dict
submit_error_response_error_dict = submit_error_response_error_instance.to_dict()
# create an instance of SubmitErrorResponseError from a dict
submit_error_response_error_from_dict = SubmitErrorResponseError.from_dict(submit_error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


