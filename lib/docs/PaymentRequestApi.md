# pluggy_sdk.PaymentRequestApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_request_create**](PaymentRequestApi.md#payment_request_create) | **POST** /payments/requests | Create
[**payment_request_create_pix_qr**](PaymentRequestApi.md#payment_request_create_pix_qr) | **POST** /payments/requests/pix-qr | Create PIX QR payment request
[**payment_request_delete**](PaymentRequestApi.md#payment_request_delete) | **DELETE** /payments/requests/{id} | Delete
[**payment_request_retrieve**](PaymentRequestApi.md#payment_request_retrieve) | **GET** /payments/requests/{id} | Retrieve
[**payment_request_update**](PaymentRequestApi.md#payment_request_update) | **PATCH** /payments/requests/{id} | Update
[**payment_requests_list**](PaymentRequestApi.md#payment_requests_list) | **GET** /payments/requests | List


# **payment_request_create**
> PaymentRequest payment_request_create(create_payment_request)

Create

Creates the payment request resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_payment_request import CreatePaymentRequest
from pluggy_sdk.models.payment_request import PaymentRequest
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
    api_instance = pluggy_sdk.PaymentRequestApi(api_client)
    create_payment_request = {"amount":100.5,"description":"Transferência"} # CreatePaymentRequest | 

    try:
        # Create
        api_response = api_instance.payment_request_create(create_payment_request)
        print("The response of PaymentRequestApi->payment_request_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestApi->payment_request_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_request** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | 

### Return type

[**PaymentRequest**](PaymentRequest.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success creating payment request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_create_pix_qr**
> PaymentRequest payment_request_create_pix_qr(create_pix_qr_payment_request)

Create PIX QR payment request

Creates the PIX QR payment request resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_pix_qr_payment_request import CreatePixQrPaymentRequest
from pluggy_sdk.models.payment_request import PaymentRequest
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
    api_instance = pluggy_sdk.PaymentRequestApi(api_client)
    create_pix_qr_payment_request = {"pixQrCode":"00020126490014br.gov.bcb.pix0108dict-key0215additional-info52040000530398654031005802BR5912example-name6006Cidade62090505tx-id63045E20","callbackUrls":null,"isSandbox":false} # CreatePixQrPaymentRequest | 

    try:
        # Create PIX QR payment request
        api_response = api_instance.payment_request_create_pix_qr(create_pix_qr_payment_request)
        print("The response of PaymentRequestApi->payment_request_create_pix_qr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestApi->payment_request_create_pix_qr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pix_qr_payment_request** | [**CreatePixQrPaymentRequest**](CreatePixQrPaymentRequest.md)|  | 

### Return type

[**PaymentRequest**](PaymentRequest.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a PIX QR payment request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_delete**
> payment_request_delete(id)

Delete

Deletes the payment request resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
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
    api_instance = pluggy_sdk.PaymentRequestApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier

    try:
        # Delete
        api_instance.payment_request_delete(id)
    except Exception as e:
        print("Exception when calling PaymentRequestApi->payment_request_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a payment request. |  -  |
**404** | Payment Request not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_retrieve**
> PaymentRequest payment_request_retrieve(id)

Retrieve

Recovers the payment request resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_request import PaymentRequest
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
    api_instance = pluggy_sdk.PaymentRequestApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier

    try:
        # Retrieve
        api_response = api_instance.payment_request_retrieve(id)
        print("The response of PaymentRequestApi->payment_request_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestApi->payment_request_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 

### Return type

[**PaymentRequest**](PaymentRequest.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a payment request. |  -  |
**404** | Payment Request not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_update**
> CreatePaymentRequest payment_request_update(id, update_payment_request)

Update

Updates the payment request resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_payment_request import CreatePaymentRequest
from pluggy_sdk.models.update_payment_request import UpdatePaymentRequest
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
    api_instance = pluggy_sdk.PaymentRequestApi(api_client)
    id = 'd0f8a8c0-e8e3-11e9-b210-d663bd873d93' # str | Payment request primary identifier
    update_payment_request = {"amount":100.5,"description":"Transferência","isSandbox":false} # UpdatePaymentRequest | 

    try:
        # Update
        api_response = api_instance.payment_request_update(id, update_payment_request)
        print("The response of PaymentRequestApi->payment_request_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestApi->payment_request_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 
 **update_payment_request** | [**UpdatePaymentRequest**](UpdatePaymentRequest.md)|  | 

### Return type

[**CreatePaymentRequest**](CreatePaymentRequest.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a payment request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_list**
> PaymentRequestsList200Response payment_requests_list(page_size=page_size, page=page, var_from=var_from, to=to, customer=customer, pix_key=pix_key)

List

Recovers all created payment requests

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_requests_list200_response import PaymentRequestsList200Response
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
    api_instance = pluggy_sdk.PaymentRequestApi(api_client)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)
    var_from = '2023-01-01' # date | Filter payment requests by start date. Returns only requests created **on or after** this date. (optional)
    to = '2024-01-01' # date | Filter payment requests by end date. Returns only requests created **on or before** this date. (optional)
    customer = 'John' # str | Filter payment requests with one customer attribute (name, email, CPF or CNPJ) (optional)
    pix_key = '11111111111' # str | Filter payment requests by Pix Key (optional)

    try:
        # List
        api_response = api_instance.payment_requests_list(page_size=page_size, page=page, var_from=var_from, to=to, customer=customer, pix_key=pix_key)
        print("The response of PaymentRequestApi->payment_requests_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestApi->payment_requests_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 
 **var_from** | **date**| Filter payment requests by start date. Returns only requests created **on or after** this date. | [optional] 
 **to** | **date**| Filter payment requests by end date. Returns only requests created **on or before** this date. | [optional] 
 **customer** | **str**| Filter payment requests with one customer attribute (name, email, CPF or CNPJ) | [optional] 
 **pix_key** | **str**| Filter payment requests by Pix Key | [optional] 

### Return type

[**PaymentRequestsList200Response**](PaymentRequestsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all payment requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

