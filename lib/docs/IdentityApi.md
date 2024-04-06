# pluggy_sdk.IdentityApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identity_find_by_item**](IdentityApi.md#identity_find_by_item) | **GET** /identity | Find by item
[**identity_retrieve**](IdentityApi.md#identity_retrieve) | **GET** /identity/{id} | Retrieve


# **identity_find_by_item**
> IdentityResponse identity_find_by_item(item_id)

Find by item

Recovers identity of an item if available

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.identity_response import IdentityResponse
from pluggy_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pluggy.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = pluggy_sdk.Configuration(
    host = "https://api.pluggy.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: default
configuration.api_key['default'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['default'] = 'Bearer'

# Enter a context with an instance of the API client
with pluggy_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pluggy_sdk.IdentityApi(api_client)
    item_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Item's primary identifier

    try:
        # Find by item
        api_response = api_instance.identity_find_by_item(item_id)
        print("The response of IdentityApi->identity_find_by_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->identity_find_by_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item&#39;s primary identifier | 

### Return type

[**IdentityResponse**](IdentityResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve an identity by itemId |  -  |
**400** | Invalid parameters |  -  |
**404** | Identity not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_retrieve**
> IdentityResponse identity_retrieve(id)

Retrieve

Recovers the identity resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.identity_response import IdentityResponse
from pluggy_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pluggy.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = pluggy_sdk.Configuration(
    host = "https://api.pluggy.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: default
configuration.api_key['default'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['default'] = 'Bearer'

# Enter a context with an instance of the API client
with pluggy_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pluggy_sdk.IdentityApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | identity primary identifier

    try:
        # Retrieve
        api_response = api_instance.identity_retrieve(id)
        print("The response of IdentityApi->identity_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->identity_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identity primary identifier | 

### Return type

[**IdentityResponse**](IdentityResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve an Identity resource. |  -  |
**400** | Invalid parameters |  -  |
**404** | Identity not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

