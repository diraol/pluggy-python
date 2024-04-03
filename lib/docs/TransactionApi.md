# openapi_client.TransactionApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_list**](TransactionApi.md#transactions_list) | **GET** /transactions | List
[**transactions_retrieve**](TransactionApi.md#transactions_retrieve) | **GET** /transactions/{id} | Retrieve
[**transactions_update**](TransactionApi.md#transactions_update) | **PATCH** /transactions/{id} | Update


# **transactions_list**
> PageResponseTransactions transactions_list(account_id, var_from=var_from, to=to, page_size=page_size, page=page)

List

Recovers all transactions collected for the acount provided

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.page_response_transactions import PageResponseTransactions
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
    api_instance = openapi_client.TransactionApi(api_client)
    account_id = '562b795d-1653-429f-be86-74ead9502813' # str | Account primary identifier
    var_from = '2020-10-13' # datetime | Filter greater than date. Format (yyyy-mm-dd) (optional)
    to = '2020-10-15' # datetime | Filter lower than date. Format (yyyy-mm-dd) (optional)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List
        api_response = api_instance.transactions_list(account_id, var_from=var_from, to=to, page_size=page_size, page=page)
        print("The response of TransactionApi->transactions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->transactions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account primary identifier | 
 **var_from** | **datetime**| Filter greater than date. Format (yyyy-mm-dd) | [optional] 
 **to** | **datetime**| Filter lower than date. Format (yyyy-mm-dd) | [optional] 
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

### Return type

[**PageResponseTransactions**](PageResponseTransactions.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all transactions for an account |  -  |
**400** | Missing parameter |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_retrieve**
> Transaction transactions_retrieve(id)

Retrieve

Recovers the transaction resource by it's id

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.transaction import Transaction
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
    api_instance = openapi_client.TransactionApi(api_client)
    id = '6ec156fe-e8ac-4d9a-a4b3-7770529ab01c' # str | transaction primary identifier

    try:
        # Retrieve
        api_response = api_instance.transactions_retrieve(id)
        print("The response of TransactionApi->transactions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->transactions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| transaction primary identifier | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a transaction. |  -  |
**404** | Transaction not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_update**
> Transaction transactions_update(id, update_transaction)

Update

Update the transaction's category by it's id

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.transaction import Transaction
from openapi_client.models.update_transaction import UpdateTransaction
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
    api_instance = openapi_client.TransactionApi(api_client)
    id = '6ec156fe-e8ac-4d9a-a4b3-7770529ab01c' # str | transaction primary identifier
    update_transaction = openapi_client.UpdateTransaction() # UpdateTransaction | New category identifier

    try:
        # Update
        api_response = api_instance.transactions_update(id, update_transaction)
        print("The response of TransactionApi->transactions_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->transactions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| transaction primary identifier | 
 **update_transaction** | [**UpdateTransaction**](UpdateTransaction.md)| New category identifier | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve an updated transaction. |  -  |
**400** | Missing parameter |  -  |
**404** | Transaction not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

