# pluggy_sdk.PortfolioYieldApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregated_portfolio_find_by_item**](PortfolioYieldApi.md#aggregated_portfolio_find_by_item) | **GET** /portfolio/{itemId} | Find aggregated portfolio yield by item
[**monthly_portfolio_find_by_item**](PortfolioYieldApi.md#monthly_portfolio_find_by_item) | **GET** /portfolio/{itemId}/monthly | Find monthly portfolio yield by item


# **aggregated_portfolio_find_by_item**
> AggregatedPortfolioResponse aggregated_portfolio_find_by_item(item_id)

Find aggregated portfolio yield by item

Recovers aggregated portfolio yield of an item if available

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.aggregated_portfolio_response import AggregatedPortfolioResponse
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
    api_instance = pluggy_sdk.PortfolioYieldApi(api_client)
    item_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Item's primary identifier

    try:
        # Find aggregated portfolio yield by item
        api_response = api_instance.aggregated_portfolio_find_by_item(item_id)
        print("The response of PortfolioYieldApi->aggregated_portfolio_find_by_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioYieldApi->aggregated_portfolio_find_by_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item&#39;s primary identifier | 

### Return type

[**AggregatedPortfolioResponse**](AggregatedPortfolioResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve the aggregated portfolio yield by itemId |  -  |
**400** | Invalid parameters |  -  |
**404** | Portgolio Yield not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monthly_portfolio_find_by_item**
> MonthlyPortfolioResponse monthly_portfolio_find_by_item(item_id)

Find monthly portfolio yield by item

Recovers monthly portfolio yield of an item if available

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.monthly_portfolio_response import MonthlyPortfolioResponse
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
    api_instance = pluggy_sdk.PortfolioYieldApi(api_client)
    item_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Item's primary identifier

    try:
        # Find monthly portfolio yield by item
        api_response = api_instance.monthly_portfolio_find_by_item(item_id)
        print("The response of PortfolioYieldApi->monthly_portfolio_find_by_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioYieldApi->monthly_portfolio_find_by_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item&#39;s primary identifier | 

### Return type

[**MonthlyPortfolioResponse**](MonthlyPortfolioResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve the monthly portfolio yield by itemId |  -  |
**400** | Invalid parameters |  -  |
**404** | Portfolio Yield not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

