# pluggy_sdk.AutomaticPIXApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_request_create_automatic_pix**](AutomaticPIXApi.md#payment_request_create_automatic_pix) | **POST** /payments/requests/automatic-pix | Create Automatic PIX payment request


# **payment_request_create_automatic_pix**
> PaymentRequest payment_request_create_automatic_pix(create_automatic_pix_payment_request)

Create Automatic PIX payment request

Creates the automatic PIX payment request resource

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
    create_automatic_pix_payment_request = {"fixedAmount":100.5,"startDate":"2025-06-10","expiresAt":"2025-10-01","isRetryAccepted":true,"firstPayment":{"date":"2025-06-10","description":"Primeiro pagamento","amount":100.5},"interval":"WEEKLY","callbackUrls":null,"recipientId":"05c693bf-c196-47ea-a28c-8251d6bb8a06"} # CreateAutomaticPixPaymentRequest | 

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

