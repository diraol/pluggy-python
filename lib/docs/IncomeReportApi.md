# openapi_client.IncomeReportApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**income_reports_find_by_item**](IncomeReportApi.md#income_reports_find_by_item) | **GET** /income-reports | Find income reports by item


# **income_reports_find_by_item**
> IncomeReportsResponse income_reports_find_by_item(item_id)

Find income reports by item

Recovers income reports of an item if available

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.income_reports_response import IncomeReportsResponse
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
    api_instance = openapi_client.IncomeReportApi(api_client)
    item_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Item's primary identifier

    try:
        # Find income reports by item
        api_response = api_instance.income_reports_find_by_item(item_id)
        print("The response of IncomeReportApi->income_reports_find_by_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomeReportApi->income_reports_find_by_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item&#39;s primary identifier | 

### Return type

[**IncomeReportsResponse**](IncomeReportsResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve income reports by itemId |  -  |
**400** | Invalid parameters |  -  |
**404** | Item not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

