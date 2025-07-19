# pluggy_sdk.AutomaticPIXApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_automatic_pix_schedule**](AutomaticPIXApi.md#cancel_automatic_pix_schedule) | **POST** /payments/requests/{id}/automatic-pix/schedules/{scheduleId}/cancel | Cancel an Automatic PIX schedule
[**payment_request_cancel_automatic_pix_consent**](AutomaticPIXApi.md#payment_request_cancel_automatic_pix_consent) | **POST** /payments/requests/{id}/automatic-pix/cancel | Cancel an automatic PIX consent
[**payment_request_create_automatic_pix**](AutomaticPIXApi.md#payment_request_create_automatic_pix) | **POST** /payments/requests/automatic-pix | Create Automatic PIX payment request
[**payment_request_create_automatic_pix_schedule**](AutomaticPIXApi.md#payment_request_create_automatic_pix_schedule) | **POST** /payments/requests/{id}/automatic-pix/schedule | Schedule Automatic PIX payment
[**payment_request_get_automatic_pix_schedule**](AutomaticPIXApi.md#payment_request_get_automatic_pix_schedule) | **GET** /payments/requests/{requestId}/automatic-pix/schedules/{paymentId} | Get an automatic PIX scheduled payment
[**payment_request_get_automatic_pix_schedules**](AutomaticPIXApi.md#payment_request_get_automatic_pix_schedules) | **GET** /payments/requests/{id}/automatic-pix/schedules | List Automatic PIX scheduled payments
[**retry_automatic_pix_schedule**](AutomaticPIXApi.md#retry_automatic_pix_schedule) | **POST** /payments/requests/{id}/automatic-pix/schedules/{scheduleId}/retry | Retry an Automatic PIX schedule


# **cancel_automatic_pix_schedule**
> cancel_automatic_pix_schedule(id, schedule_id)

Cancel an Automatic PIX schedule

Cancels an Automatic PIX schedule.

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
    api_instance = pluggy_sdk.AutomaticPIXApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier
    schedule_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Automatic PIX schedule primary identifier

    try:
        # Cancel an Automatic PIX schedule
        api_instance.cancel_automatic_pix_schedule(id, schedule_id)
    except Exception as e:
        print("Exception when calling AutomaticPIXApi->cancel_automatic_pix_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 
 **schedule_id** | **str**| Automatic PIX schedule primary identifier | 

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_cancel_automatic_pix_consent**
> payment_request_cancel_automatic_pix_consent(id)

Cancel an automatic PIX consent

Cancels an automatic PIX consent

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
    api_instance = pluggy_sdk.AutomaticPIXApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier

    try:
        # Cancel an automatic PIX consent
        api_instance.payment_request_cancel_automatic_pix_consent(id)
    except Exception as e:
        print("Exception when calling AutomaticPIXApi->payment_request_cancel_automatic_pix_consent: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_create_automatic_pix**
> PaymentRequest payment_request_create_automatic_pix(create_automatic_pix_payment_request)

Create Automatic PIX payment request

Creates a payment request where the payment is made using automatic PIX. Once consent is granted by the user, payments can be scheduled according to the rules defined in the request.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_automatic_pix_payment_request import CreateAutomaticPixPaymentRequest
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
    api_instance = pluggy_sdk.AutomaticPIXApi(api_client)
    create_automatic_pix_payment_request = {"fixedAmount":100.5,"startDate":"2025-06-10","expiresAt":"2025-10-01T03:00:00Z","isRetryAccepted":true,"firstPayment":{"date":"2025-06-10","description":"Primeiro pagamento","amount":100.5},"interval":"WEEKLY","callbackUrls":null,"recipientId":"05c693bf-c196-47ea-a28c-8251d6bb8a06","isSandbox":false} # CreateAutomaticPixPaymentRequest | 

    try:
        # Create Automatic PIX payment request
        api_response = api_instance.payment_request_create_automatic_pix(create_automatic_pix_payment_request)
        print("The response of AutomaticPIXApi->payment_request_create_automatic_pix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomaticPIXApi->payment_request_create_automatic_pix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_automatic_pix_payment_request** | [**CreateAutomaticPixPaymentRequest**](CreateAutomaticPixPaymentRequest.md)|  | 

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
**200** | Create a Automatic PIX payment request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_create_automatic_pix_schedule**
> AutomaticPixPayment payment_request_create_automatic_pix_schedule(id, schedule_automatic_pix_payment_request)

Schedule Automatic PIX payment

Schedules an Automatic PIX payment

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.automatic_pix_payment import AutomaticPixPayment
from pluggy_sdk.models.schedule_automatic_pix_payment_request import ScheduleAutomaticPixPaymentRequest
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
    api_instance = pluggy_sdk.AutomaticPIXApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier
    schedule_automatic_pix_payment_request = {"amount":100.5,"date":"2025-06-10","description":"Transferência","clientPaymentId":"external-ref-456","isSandbox":false} # ScheduleAutomaticPixPaymentRequest | 

    try:
        # Schedule Automatic PIX payment
        api_response = api_instance.payment_request_create_automatic_pix_schedule(id, schedule_automatic_pix_payment_request)
        print("The response of AutomaticPIXApi->payment_request_create_automatic_pix_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomaticPIXApi->payment_request_create_automatic_pix_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 
 **schedule_automatic_pix_payment_request** | [**ScheduleAutomaticPixPaymentRequest**](ScheduleAutomaticPixPaymentRequest.md)|  | 

### Return type

[**AutomaticPixPayment**](AutomaticPixPayment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schedule a Automatic PIX payment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_get_automatic_pix_schedule**
> AutomaticPixPayment payment_request_get_automatic_pix_schedule(request_id, payment_id)

Get an automatic PIX scheduled payment

Recovers an automatic PIX scheduled payment by id

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
    api_instance = pluggy_sdk.AutomaticPIXApi(api_client)
    request_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier
    payment_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Automatic PIX scheduled payment primary identifier

    try:
        # Get an automatic PIX scheduled payment
        api_response = api_instance.payment_request_get_automatic_pix_schedule(request_id, payment_id)
        print("The response of AutomaticPIXApi->payment_request_get_automatic_pix_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomaticPIXApi->payment_request_get_automatic_pix_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Payment request primary identifier | 
 **payment_id** | **str**| Automatic PIX scheduled payment primary identifier | 

### Return type

[**AutomaticPixPayment**](AutomaticPixPayment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recovers an automatic PIX scheduled payment by id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_request_get_automatic_pix_schedules**
> PaymentRequestGetAutomaticPixSchedules200Response payment_request_get_automatic_pix_schedules(id)

List Automatic PIX scheduled payments

Lists all Automatic PIX payments from a payment request

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_request_get_automatic_pix_schedules200_response import PaymentRequestGetAutomaticPixSchedules200Response
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
    api_instance = pluggy_sdk.AutomaticPIXApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier

    try:
        # List Automatic PIX scheduled payments
        api_response = api_instance.payment_request_get_automatic_pix_schedules(id)
        print("The response of AutomaticPIXApi->payment_request_get_automatic_pix_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomaticPIXApi->payment_request_get_automatic_pix_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 

### Return type

[**PaymentRequestGetAutomaticPixSchedules200Response**](PaymentRequestGetAutomaticPixSchedules200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recovers all automatic PIX payments from a payment request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_automatic_pix_schedule**
> retry_automatic_pix_schedule(id, schedule_id, retry_automatic_pix_payment_request)

Retry an Automatic PIX schedule

Retries an Automatic PIX schedule, only if the authorization accepts retries. The system allows up to 3 retry attempts. Requests must be submitted by 10pm on the day before the scheduled payment date.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.retry_automatic_pix_payment_request import RetryAutomaticPixPaymentRequest
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
    api_instance = pluggy_sdk.AutomaticPIXApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier
    schedule_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Automatic PIX schedule primary identifier
    retry_automatic_pix_payment_request = {"date":"2025-06-10","isSandbox":false} # RetryAutomaticPixPaymentRequest | 

    try:
        # Retry an Automatic PIX schedule
        api_instance.retry_automatic_pix_schedule(id, schedule_id, retry_automatic_pix_payment_request)
    except Exception as e:
        print("Exception when calling AutomaticPIXApi->retry_automatic_pix_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment request primary identifier | 
 **schedule_id** | **str**| Automatic PIX schedule primary identifier | 
 **retry_automatic_pix_payment_request** | [**RetryAutomaticPixPaymentRequest**](RetryAutomaticPixPaymentRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

