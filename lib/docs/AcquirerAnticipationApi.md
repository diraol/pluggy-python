# openapi_client.AcquirerAnticipationApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquirer_anticipation_retrieve**](AcquirerAnticipationApi.md#acquirer_anticipation_retrieve) | **GET** /acquirer-anticipations/{id} | Retrieve
[**acquirer_anticipations_list**](AcquirerAnticipationApi.md#acquirer_anticipations_list) | **GET** /acquirer-anticipations | List


# **acquirer_anticipation_retrieve**
> AcquirerAnticipation acquirer_anticipation_retrieve(id)

Retrieve

Recovers the acquirer anticipation resource by it's id

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.acquirer_anticipation import AcquirerAnticipation
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
    api_instance = openapi_client.AcquirerAnticipationApi(api_client)
    id = '6ec156fe-e8ac-4d9a-a4b3-7770529ab01c' # str | Acquirer anticipation primary identifier

    try:
        # Retrieve
        api_response = api_instance.acquirer_anticipation_retrieve(id)
        print("The response of AcquirerAnticipationApi->acquirer_anticipation_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcquirerAnticipationApi->acquirer_anticipation_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Acquirer anticipation primary identifier | 

### Return type

[**AcquirerAnticipation**](AcquirerAnticipation.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a acquirer anticipation. |  -  |
**404** | Acquirer Anticipation not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquirer_anticipations_list**
> PageResponseAcquirerAnticipations acquirer_anticipations_list(item_id, var_from=var_from, to=to, page_size=page_size, page=page)

List

Recovers all acquirer anticipations collected for the item provided

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.page_response_acquirer_anticipations import PageResponseAcquirerAnticipations
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
    api_instance = openapi_client.AcquirerAnticipationApi(api_client)
    item_id = '562b795d-1653-429f-be86-74ead9502813' # str | Item primary identifier
    var_from = '2020-10-13' # datetime | Filter greater than date. Format (yyyy-mm-dd) (optional)
    to = '2020-10-15' # datetime | Filter lower than date. Format (yyyy-mm-dd) (optional)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List
        api_response = api_instance.acquirer_anticipations_list(item_id, var_from=var_from, to=to, page_size=page_size, page=page)
        print("The response of AcquirerAnticipationApi->acquirer_anticipations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcquirerAnticipationApi->acquirer_anticipations_list: %s\n" % e)
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

[**PageResponseAcquirerAnticipations**](PageResponseAcquirerAnticipations.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all acquirer anticipations for a item |  -  |
**400** | Missing parameter |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

