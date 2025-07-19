# pluggy_sdk.PaymentIntentApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_intent_create**](PaymentIntentApi.md#payment_intent_create) | **POST** /payments/intents | Create
[**payment_intent_retrieve**](PaymentIntentApi.md#payment_intent_retrieve) | **GET** /payments/intents/{id} | Retrieve
[**payment_intents_list**](PaymentIntentApi.md#payment_intents_list) | **GET** /payments/intents | List


# **payment_intent_create**
> PaymentIntent payment_intent_create(create_payment_intent)

Create

Creates the payment intent resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_payment_intent import CreatePaymentIntent
from pluggy_sdk.models.payment_intent import PaymentIntent
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
    api_instance = pluggy_sdk.PaymentIntentApi(api_client)
    create_payment_intent = {"paymentRequestId":"c2a6b7d9-3349-435d-8341-44021449ebbc","connectorId":603,"parameters":{"cpf":"11111111111"},"isSandbox":false} # CreatePaymentIntent | 

    try:
        # Create
        api_response = api_instance.payment_intent_create(create_payment_intent)
        print("The response of PaymentIntentApi->payment_intent_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentIntentApi->payment_intent_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_intent** | [**CreatePaymentIntent**](CreatePaymentIntent.md)|  | 

### Return type

[**PaymentIntent**](PaymentIntent.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a payment intent. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_intent_retrieve**
> PaymentIntent payment_intent_retrieve(id)

Retrieve

Recovers the payment intent resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_intent import PaymentIntent
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
    api_instance = pluggy_sdk.PaymentIntentApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment intent primary identifier

    try:
        # Retrieve
        api_response = api_instance.payment_intent_retrieve(id)
        print("The response of PaymentIntentApi->payment_intent_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentIntentApi->payment_intent_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment intent primary identifier | 

### Return type

[**PaymentIntent**](PaymentIntent.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a payment intent. |  -  |
**404** | Payment Intent not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_intents_list**
> PaymentIntentsList200Response payment_intents_list(payment_request_id)

List

Recovers all created payment intents for the payment request provided

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_intents_list200_response import PaymentIntentsList200Response
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
    api_instance = pluggy_sdk.PaymentIntentApi(api_client)
    payment_request_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment request primary identifier

    try:
        # List
        api_response = api_instance.payment_intents_list(payment_request_id)
        print("The response of PaymentIntentApi->payment_intents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentIntentApi->payment_intents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| Payment request primary identifier | 

### Return type

[**PaymentIntentsList200Response**](PaymentIntentsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all payment intents for the payment request provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

