# openapi_client.PetApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_pets**](PetApi.md#list_pets) | **GET** /pets | List all pets


# **list_pets**
> List[Pet] list_pets()

List all pets

### Example


```python
import openapi_client
from openapi_client.models.pet import Pet
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PetApi(api_client)

    try:
        # List all pets
        api_response = api_instance.list_pets()
        print("The response of PetApi->list_pets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetApi->list_pets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Pet]**](Pet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of pets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

