# openapi_client.InvestmentApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**investment_transactions_list**](InvestmentApi.md#investment_transactions_list) | **GET** /investments/{id}/transactions | List investment transactions
[**investments_list**](InvestmentApi.md#investments_list) | **GET** /investments | List
[**investments_retrieve**](InvestmentApi.md#investments_retrieve) | **GET** /investments/{id} | Retrieve


# **investment_transactions_list**
> PageResponseInvestmentTransactions investment_transactions_list(id, page_size=page_size, page=page)

List investment transactions

Recovers all investment transactions for the investment provided

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.page_response_investment_transactions import PageResponseInvestmentTransactions
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
    api_instance = openapi_client.InvestmentApi(api_client)
    id = '562b795d-1653-429f-be86-74ead9502813' # str | Investment primary identifier
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List investment transactions
        api_response = api_instance.investment_transactions_list(id, page_size=page_size, page=page)
        print("The response of InvestmentApi->investment_transactions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentApi->investment_transactions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Investment primary identifier | 
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

### Return type

[**PageResponseInvestmentTransactions**](PageResponseInvestmentTransactions.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all transactions for an investment |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **investments_list**
> InvestmentsList200Response investments_list(item_id, type=type, page_size=page_size, page=page)

List

Recovers all investments collected for the item provided

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.investments_list200_response import InvestmentsList200Response
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
    api_instance = openapi_client.InvestmentApi(api_client)
    item_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Item's primary identifier
    type = 'type_example' # str | Investment's type to filter (optional)
    page_size = 50 # float | Page size for the paging request, default: 500 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List
        api_response = api_instance.investments_list(item_id, type=type, page_size=page_size, page=page)
        print("The response of InvestmentApi->investments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentApi->investments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item&#39;s primary identifier | 
 **type** | **str**| Investment&#39;s type to filter | [optional] 
 **page_size** | **float**| Page size for the paging request, default: 500 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

### Return type

[**InvestmentsList200Response**](InvestmentsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all investments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **investments_retrieve**
> Investment investments_retrieve(id)

Retrieve

Recovers the investment resource by its id

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.investment import Investment
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
    api_instance = openapi_client.InvestmentApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | investment primary identifier

    try:
        # Retrieve
        api_response = api_instance.investments_retrieve(id)
        print("The response of InvestmentApi->investments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentApi->investments_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| investment primary identifier | 

### Return type

[**Investment**](Investment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve an investment. |  -  |
**404** | Investment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

