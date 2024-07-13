# pluggy_sdk.PaymentReceiptsApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_request_receipt_create**](PaymentReceiptsApi.md#payment_request_receipt_create) | **POST** /payments/requests/{id}/receipts | Create Payment Receipt
[**payment_request_receipt_list**](PaymentReceiptsApi.md#payment_request_receipt_list) | **GET** /payments/requests/{id}/receipts | List Payment Receipts
[**payment_request_receipt_retrieve**](PaymentReceiptsApi.md#payment_request_receipt_retrieve) | **GET** /payments/requests/{payment-request-id}/receipts/{payment-receipt-id} | Retrieve Payment Receipt


# **payment_request_receipt_create**
> PaymentReceipt payment_request_receipt_create(id)

Create Payment Receipt

Creates the payment receipt resource

### Example


```python
import pluggy_sdk
from pluggy_sdk.models.payment_receipt import PaymentReceipt
from pluggy_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pluggy.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = pluggy_sdk.Configuration(
    host = "https://api.pluggy.ai"
)


# Enter a context with an instance of the API client
with pluggy_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pluggy_sdk.PaymentReceiptsApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier

    try:
        # Create Payment Receipt
        api_response = api_instance.payment_request_receipt_create(id)
        print("The response of PaymentReceiptsApi->payment_request_receipt_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentReceiptsApi->payment_request_receipt_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 

### Return type

[**PaymentReceipt**](PaymentReceipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success creating payment receipt |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_receipt_list**
> PaymentRequestReceiptList200Response payment_request_receipt_list(id)

List Payment Receipts

Recovers all created payment receipts for the payment request provided

### Example


```python
import pluggy_sdk
from pluggy_sdk.models.payment_request_receipt_list200_response import PaymentRequestReceiptList200Response
from pluggy_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pluggy.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = pluggy_sdk.Configuration(
    host = "https://api.pluggy.ai"
)


# Enter a context with an instance of the API client
with pluggy_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pluggy_sdk.PaymentReceiptsApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier

    try:
        # List Payment Receipts
        api_response = api_instance.payment_request_receipt_list(id)
        print("The response of PaymentReceiptsApi->payment_request_receipt_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentReceiptsApi->payment_request_receipt_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 

### Return type

[**PaymentRequestReceiptList200Response**](PaymentRequestReceiptList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all payment receipts for the payment request provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_receipt_retrieve**
> PaymentReceipt payment_request_receipt_retrieve(payment_request_id, payment_receipt_id)

Retrieve Payment Receipt

Recovers the payment receipt resource by its id

### Example


```python
import pluggy_sdk
from pluggy_sdk.models.payment_receipt import PaymentReceipt
from pluggy_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pluggy.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = pluggy_sdk.Configuration(
    host = "https://api.pluggy.ai"
)


# Enter a context with an instance of the API client
with pluggy_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pluggy_sdk.PaymentReceiptsApi(api_client)
    payment_request_id = 'payment_request_id_example' # str | 
    payment_receipt_id = 'payment_receipt_id_example' # str | 

    try:
        # Retrieve Payment Receipt
        api_response = api_instance.payment_request_receipt_retrieve(payment_request_id, payment_receipt_id)
        print("The response of PaymentReceiptsApi->payment_request_receipt_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentReceiptsApi->payment_request_receipt_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**|  | 
 **payment_receipt_id** | **str**|  | 

### Return type

[**PaymentReceipt**](PaymentReceipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a payment receipt. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

