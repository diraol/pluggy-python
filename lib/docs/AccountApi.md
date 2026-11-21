# pluggy_sdk.AccountApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_balance_get**](AccountApi.md#account_balance_get) | **GET** /accounts/{id}/balance | Get real-time balance
[**accounts_list**](AccountApi.md#accounts_list) | **GET** /accounts | List
[**accounts_retrieve**](AccountApi.md#accounts_retrieve) | **GET** /accounts/{id} | Retrieve


# **account_balance_get**
> AccountBalanceGet200Response account_balance_get(id)

Get real-time balance

Fetches the real-time balance for the account directly from the financial institution connector, without requiring a full item sync. Requires the API key (`X-API-KEY`): a Connect Token `accessToken` is rejected with 403 `FORBIDDEN_INSUFFICIENT_PERMISSIONS`.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.account_balance_get200_response import AccountBalanceGet200Response
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
    api_instance = pluggy_sdk.AccountApi(api_client)
    id = 'a658c848-e475-457b-8565-d1fffba127c4' # str | Account primary identifier

    try:
        # Get real-time balance
        api_response = api_instance.account_balance_get(id)
        print("The response of AccountApi->account_balance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_balance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Account primary identifier | 

### Return type

[**AccountBalanceGet200Response**](AccountBalanceGet200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Real-time account balance |  -  |
**400** | The balance request was rejected as invalid by the financial institution |  -  |
**403** | The financial institution rejected the consent&#39;s access token or denied access to the account balance (&#x60;BALANCE_CONSENT_ERROR&#x60;; the consent may be expired, revoked or missing the required permission, so the user may need to reconnect), or the request used a Connect Token instead of the API key (&#x60;FORBIDDEN_INSUFFICIENT_PERMISSIONS&#x60;) |  -  |
**404** | Account not found, or the balance was not found at the financial institution |  -  |
**429** | Rate limited by the financial institution |  -  |
**500** | Unexpected error fetching balance from connector |  -  |
**502** | The financial institution is temporarily unavailable to provide the balance |  -  |
**503** | The financial institution reached its global Open Finance request limit and is temporarily not answering balance requests (&#x60;BALANCE_INSTITUTION_RATE_LIMITED&#x60;). The limit covers all traffic the institution receives, not your application: nothing is wrong with the request or the consent. No &#x60;Retry-After&#x60; is sent because the institution does not provide one; retry later with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_list**
> AccountsList200Response accounts_list(item_id, type=type, page_size=page_size, page=page)

List

Recovers all accounts collected for the item provided

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.accounts_list200_response import AccountsList200Response
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
    api_instance = pluggy_sdk.AccountApi(api_client)
    item_id = UUID('d0f8a8c0-e8e3-11e9-b210-d663bd873d93') # UUID | Item primary identifier
    type = 'BANK' # str | Parameter to filter between bank accounts and credit accounts (optional)
    page_size = 50 # float | Page size for the paging request, default: 500. Maximum: 500 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List
        api_response = api_instance.accounts_list(item_id, type=type, page_size=page_size, page=page)
        print("The response of AccountApi->accounts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->accounts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **UUID**| Item primary identifier | 
 **type** | **str**| Parameter to filter between bank accounts and credit accounts | [optional] 
 **page_size** | **float**| Page size for the paging request, default: 500. Maximum: 500 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

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
import pluggy_sdk
from pluggy_sdk.models.account import Account
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
    api_instance = pluggy_sdk.AccountApi(api_client)
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

