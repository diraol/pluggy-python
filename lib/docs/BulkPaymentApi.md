# openapi_client.BulkPaymentApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_payment_create**](BulkPaymentApi.md#bulk_payment_create) | **POST** /payments/bulk | Create
[**bulk_payment_retrieve**](BulkPaymentApi.md#bulk_payment_retrieve) | **GET** /payments/bulk/{id} | Retrieve
[**bulk_payments_list**](BulkPaymentApi.md#bulk_payments_list) | **GET** /payments/bulk | List


# **bulk_payment_create**
> BulkPayment bulk_payment_create(create_bulk_payment)

Create

Creates the bulk payment resource

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.bulk_payment import BulkPayment
from openapi_client.models.create_bulk_payment import CreateBulkPayment
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
    api_instance = openapi_client.BulkPaymentApi(api_client)
    create_bulk_payment = openapi_client.CreateBulkPayment() # CreateBulkPayment | 

    try:
        # Create
        api_response = api_instance.bulk_payment_create(create_bulk_payment)
        print("The response of BulkPaymentApi->bulk_payment_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkPaymentApi->bulk_payment_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bulk_payment** | [**CreateBulkPayment**](CreateBulkPayment.md)|  | 

### Return type

[**BulkPayment**](BulkPayment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a Bulk Payment. |  -  |
**400** | Bulk Payment is Invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_payment_retrieve**
> BulkPayment bulk_payment_retrieve(id)

Retrieve

Recovers the bulk payment resource by its id

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.bulk_payment import BulkPayment
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
    api_instance = openapi_client.BulkPaymentApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Bulk payment primary identifier

    try:
        # Retrieve
        api_response = api_instance.bulk_payment_retrieve(id)
        print("The response of BulkPaymentApi->bulk_payment_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkPaymentApi->bulk_payment_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bulk payment primary identifier | 

### Return type

[**BulkPayment**](BulkPayment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a bulk payment |  -  |
**404** | Bulk payment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_payments_list**
> BulkPaymentsList200Response bulk_payments_list(page_size=page_size, page=page)

List

Recovers all created bulk payments

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.bulk_payments_list200_response import BulkPaymentsList200Response
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
    api_instance = openapi_client.BulkPaymentApi(api_client)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List
        api_response = api_instance.bulk_payments_list(page_size=page_size, page=page)
        print("The response of BulkPaymentApi->bulk_payments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkPaymentApi->bulk_payments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

### Return type

[**BulkPaymentsList200Response**](BulkPaymentsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all bulk payments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

