# pluggy_sdk.AcquirerSaleApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquirer_sales_list**](AcquirerSaleApi.md#acquirer_sales_list) | **GET** /acquirer-sales | List
[**acquirer_sales_retrieve**](AcquirerSaleApi.md#acquirer_sales_retrieve) | **GET** /acquirer-sales/{id} | Retrieve


# **acquirer_sales_list**
> PageResponseAcquirerSales acquirer_sales_list(item_id, var_from=var_from, to=to, page_size=page_size, page=page)

List

Recovers all acquirer sales collected for the item provided

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.page_response_acquirer_sales import PageResponseAcquirerSales
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
    api_instance = pluggy_sdk.AcquirerSaleApi(api_client)
    item_id = '562b795d-1653-429f-be86-74ead9502813' # str | Item primary identifier
    var_from = '2020-10-13' # datetime | Filter greater than date. Format (yyyy-mm-dd) (optional)
    to = '2020-10-15' # datetime | Filter lower than date. Format (yyyy-mm-dd) (optional)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List
        api_response = api_instance.acquirer_sales_list(item_id, var_from=var_from, to=to, page_size=page_size, page=page)
        print("The response of AcquirerSaleApi->acquirer_sales_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcquirerSaleApi->acquirer_sales_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item primary identifier | 
 **var_from** | **datetime**| Filter greater than date. Format (yyyy-mm-dd) | [optional] 
 **to** | **datetime**| Filter lower than date. Format (yyyy-mm-dd) | [optional] 
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

### Return type

[**PageResponseAcquirerSales**](PageResponseAcquirerSales.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all acquirer sales for a item |  -  |
**400** | Missing parameter |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquirer_sales_retrieve**
> AcquirerSale acquirer_sales_retrieve(id)

Retrieve

Recovers the acquirer sale resource by it's id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.acquirer_sale import AcquirerSale
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
    api_instance = pluggy_sdk.AcquirerSaleApi(api_client)
    id = '6ec156fe-e8ac-4d9a-a4b3-7770529ab01c' # str | Acquirer sale primary identifier

    try:
        # Retrieve
        api_response = api_instance.acquirer_sales_retrieve(id)
        print("The response of AcquirerSaleApi->acquirer_sales_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcquirerSaleApi->acquirer_sales_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Acquirer sale primary identifier | 

### Return type

[**AcquirerSale**](AcquirerSale.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a acquirer sale. |  -  |
**404** | Acquirer Sale not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

