# openapi_client.DefaultApi

All URIs are relative to *https://s1.ripple.com:51234*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_ost**](DefaultApi.md#p_ost) | **POST** / | Send JSON-RPC request to server


# **p_ost**
> POST200Response p_ost(post_request)

Send JSON-RPC request to server

### Example


```python
import openapi_client
from openapi_client.models.post200_response import POST200Response
from openapi_client.models.post_request import POSTRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://s1.ripple.com:51234
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://s1.ripple.com:51234"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    post_request = openapi_client.POSTRequest() # POSTRequest | JSON-RPC request object

    try:
        # Send JSON-RPC request to server
        api_response = api_instance.p_ost(post_request)
        print("The response of DefaultApi->p_ost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->p_ost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_request** | [**POSTRequest**](POSTRequest.md)| JSON-RPC request object | 

### Return type

[**POST200Response**](POST200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON-RPC response object |  -  |
**503** | An error for when the client is over the server&#39;s rate limit. |  -  |
**4XX** | JSON-RPC http error. The response is a plain-text explanation with the http error code and description in the response body. |  -  |
**5XX** | JSON-RPC http error. The response is a plain-text explanation with the http error code and description in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

