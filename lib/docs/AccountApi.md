# openapi_client.AccountApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_list**](AccountApi.md#accounts_list) | **GET** /accounts | List
[**accounts_retrieve**](AccountApi.md#accounts_retrieve) | **GET** /accounts/{id} | Retrieve


# **accounts_list**
> AccountsList200Response accounts_list(item_id, type=type)

List

Recovers all accounts collected for the item provided

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.accounts_list200_response import AccountsList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pluggy.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountApi(api_client)
    item_id = 'd0f8a8c0-e8e3-11e9-b210-d663bd873d93' # str | Item primary identifier
    type = 'BANK' # str | Parameter to filter between bank accounts and credit accounts (optional)

    try:
        # List
        api_response = api_instance.accounts_list(item_id, type=type)
        print("The response of AccountApi->accounts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->accounts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item primary identifier | 
 **type** | **str**| Parameter to filter between bank accounts and credit accounts | [optional] 

### Return type

[**AccountsList200Response**](AccountsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_retrieve**
> Account accounts_retrieve(id)

Retrieve

Recovers the account resource by its id

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.account import Account
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pluggy.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountApi(api_client)
    id = 'a658c848-e475-457b-8565-d1fffba127c4' # str | Account primary identifier

    try:
        # Retrieve
        api_response = api_instance.accounts_retrieve(id)
        print("The response of AccountApi->accounts_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->accounts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Account primary identifier | 

### Return type

[**Account**](Account.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve an account. |  -  |
**404** | Account not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

