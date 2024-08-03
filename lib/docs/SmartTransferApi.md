# pluggy_sdk.SmartTransferApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_tranfers_preauthorizations_list**](SmartTransferApi.md#smart_tranfers_preauthorizations_list) | **GET** /smart-transfers/preauthorizations | List preauthorizations
[**smart_transfer_payment_create**](SmartTransferApi.md#smart_transfer_payment_create) | **POST** /smart-transfers/payments | Create payment
[**smart_transfer_paymentretrieve**](SmartTransferApi.md#smart_transfer_paymentretrieve) | **GET** /smart-transfers/payments/{id} | Retrieve payment
[**smart_transfer_preauthorization_create**](SmartTransferApi.md#smart_transfer_preauthorization_create) | **POST** /smart-transfers/preauthorizations | Create preauthorization
[**smart_transfer_preauthorization_retrieve**](SmartTransferApi.md#smart_transfer_preauthorization_retrieve) | **GET** /smart-transfers/preauthorizations/{id} | Retrieve preauthorization


# **smart_tranfers_preauthorizations_list**
> SmartTranfersPreauthorizationsList200Response smart_tranfers_preauthorizations_list(page_size=page_size, page=page)

List preauthorizations

Recovers all created preauthorizations

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.smart_tranfers_preauthorizations_list200_response import SmartTranfersPreauthorizationsList200Response
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
    api_instance = pluggy_sdk.SmartTransferApi(api_client)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List preauthorizations
        api_response = api_instance.smart_tranfers_preauthorizations_list(page_size=page_size, page=page)
        print("The response of SmartTransferApi->smart_tranfers_preauthorizations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->smart_tranfers_preauthorizations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

### Return type

[**SmartTranfersPreauthorizationsList200Response**](SmartTranfersPreauthorizationsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all preauthorizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_transfer_payment_create**
> SmartTransferPayment smart_transfer_payment_create(create_smart_transfer_payment)

Create payment

Creates the smart transfer payment resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_smart_transfer_payment import CreateSmartTransferPayment
from pluggy_sdk.models.smart_transfer_payment import SmartTransferPayment
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
    api_instance = pluggy_sdk.SmartTransferApi(api_client)
    create_smart_transfer_payment = pluggy_sdk.CreateSmartTransferPayment() # CreateSmartTransferPayment | 

    try:
        # Create payment
        api_response = api_instance.smart_transfer_payment_create(create_smart_transfer_payment)
        print("The response of SmartTransferApi->smart_transfer_payment_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->smart_transfer_payment_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_smart_transfer_payment** | [**CreateSmartTransferPayment**](CreateSmartTransferPayment.md)|  | 

### Return type

[**SmartTransferPayment**](SmartTransferPayment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a Smart Transfer Payment. |  -  |
**400** | Payment is Invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_transfer_paymentretrieve**
> SmartTransferPayment smart_transfer_paymentretrieve(id)

Retrieve payment

Recovers the smart transfer payment resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.smart_transfer_payment import SmartTransferPayment
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
    api_instance = pluggy_sdk.SmartTransferApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment primary identifier

    try:
        # Retrieve payment
        api_response = api_instance.smart_transfer_paymentretrieve(id)
        print("The response of SmartTransferApi->smart_transfer_paymentretrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->smart_transfer_paymentretrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment primary identifier | 

### Return type

[**SmartTransferPayment**](SmartTransferPayment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a payment |  -  |
**404** | Smart Transfer Payment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_transfer_preauthorization_create**
> SmartTransferPreauthorization smart_transfer_preauthorization_create(create_smart_transfer_preauthorization)

Create preauthorization

Creates the smart transfer preauthorization resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_smart_transfer_preauthorization import CreateSmartTransferPreauthorization
from pluggy_sdk.models.smart_transfer_preauthorization import SmartTransferPreauthorization
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
    api_instance = pluggy_sdk.SmartTransferApi(api_client)
    create_smart_transfer_preauthorization = pluggy_sdk.CreateSmartTransferPreauthorization() # CreateSmartTransferPreauthorization | 

    try:
        # Create preauthorization
        api_response = api_instance.smart_transfer_preauthorization_create(create_smart_transfer_preauthorization)
        print("The response of SmartTransferApi->smart_transfer_preauthorization_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->smart_transfer_preauthorization_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_smart_transfer_preauthorization** | [**CreateSmartTransferPreauthorization**](CreateSmartTransferPreauthorization.md)|  | 

### Return type

[**SmartTransferPreauthorization**](SmartTransferPreauthorization.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a Smart Transfer Preauthorization. |  -  |
**400** | Preauthorization is Invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_transfer_preauthorization_retrieve**
> SmartTransferPreauthorization smart_transfer_preauthorization_retrieve(id)

Retrieve preauthorization

Recovers the smart transfer preauthorization resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.smart_transfer_preauthorization import SmartTransferPreauthorization
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
    api_instance = pluggy_sdk.SmartTransferApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Preauthorization primary identifier

    try:
        # Retrieve preauthorization
        api_response = api_instance.smart_transfer_preauthorization_retrieve(id)
        print("The response of SmartTransferApi->smart_transfer_preauthorization_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->smart_transfer_preauthorization_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Preauthorization primary identifier | 

### Return type

[**SmartTransferPreauthorization**](SmartTransferPreauthorization.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a preauthorization |  -  |
**404** | Smart Transfer Preauthorization not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

