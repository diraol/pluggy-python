# pluggy_sdk.SmartAccountApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_account_balance_retrieve**](SmartAccountApi.md#smart_account_balance_retrieve) | **GET** /payments/smart-accounts/{id}/balance | Retrieve Balance
[**smart_account_create**](SmartAccountApi.md#smart_account_create) | **POST** /payments/smart-accounts | Create
[**smart_account_retrieve**](SmartAccountApi.md#smart_account_retrieve) | **GET** /payments/smart-accounts/{id} | Retrieve
[**smart_accounts_list**](SmartAccountApi.md#smart_accounts_list) | **GET** /payments/smart-accounts | List


# **smart_account_balance_retrieve**
> SmartAccountBalance smart_account_balance_retrieve(id)

Retrieve Balance

Recovers the smart account balance resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.smart_account_balance import SmartAccountBalance
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
    api_instance = pluggy_sdk.SmartAccountApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Smart account primary identifier

    try:
        # Retrieve Balance
        api_response = api_instance.smart_account_balance_retrieve(id)
        print("The response of SmartAccountApi->smart_account_balance_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartAccountApi->smart_account_balance_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Smart account primary identifier | 

### Return type

[**SmartAccountBalance**](SmartAccountBalance.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a smart account balance |  -  |
**404** | Smart account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_account_create**
> SmartAccount smart_account_create(create_smart_account_request)

Create

Creates the smart account resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_smart_account_request import CreateSmartAccountRequest
from pluggy_sdk.models.smart_account import SmartAccount
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
    api_instance = pluggy_sdk.SmartAccountApi(api_client)
    create_smart_account_request = pluggy_sdk.CreateSmartAccountRequest() # CreateSmartAccountRequest | 

    try:
        # Create
        api_response = api_instance.smart_account_create(create_smart_account_request)
        print("The response of SmartAccountApi->smart_account_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartAccountApi->smart_account_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_smart_account_request** | [**CreateSmartAccountRequest**](CreateSmartAccountRequest.md)|  | 

### Return type

[**SmartAccount**](SmartAccount.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a smart account. |  -  |
**400** | Smart account is Invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_account_retrieve**
> SmartAccount smart_account_retrieve(id)

Retrieve

Recovers the smart account resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.smart_account import SmartAccount
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
    api_instance = pluggy_sdk.SmartAccountApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Smart account primary identifier

    try:
        # Retrieve
        api_response = api_instance.smart_account_retrieve(id)
        print("The response of SmartAccountApi->smart_account_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartAccountApi->smart_account_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Smart account primary identifier | 

### Return type

[**SmartAccount**](SmartAccount.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a smart account |  -  |
**404** | Smart account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_accounts_list**
> SmartAccountsList200Response smart_accounts_list(page_size=page_size, page=page)

List

Recovers all created smart accounts

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.smart_accounts_list200_response import SmartAccountsList200Response
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
    api_instance = pluggy_sdk.SmartAccountApi(api_client)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List
        api_response = api_instance.smart_accounts_list(page_size=page_size, page=page)
        print("The response of SmartAccountApi->smart_accounts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartAccountApi->smart_accounts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

### Return type

[**SmartAccountsList200Response**](SmartAccountsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all smart accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

