# pluggy_sdk.SmartAccountTransferApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_account_transfer**](SmartAccountTransferApi.md#smart_account_transfer) | **GET** /payments/smart-accounts/{id}/transfers/{transfer_id} | Retrieve Transfer
[**smart_account_transfer_create**](SmartAccountTransferApi.md#smart_account_transfer_create) | **POST** /payments/smart-accounts/{id}/transfers | Create Transfer


# **smart_account_transfer**
> SmartAccountTransfer smart_account_transfer(id, transfer_id)

Retrieve Transfer

Get a transfer from the smart account

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.smart_account_transfer import SmartAccountTransfer
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
    api_instance = pluggy_sdk.SmartAccountTransferApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Smart account primary identifier
    transfer_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Transfer primary identifier

    try:
        # Retrieve Transfer
        api_response = api_instance.smart_account_transfer(id, transfer_id)
        print("The response of SmartAccountTransferApi->smart_account_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartAccountTransferApi->smart_account_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Smart account primary identifier | 
 **transfer_id** | **str**| Transfer primary identifier | 

### Return type

[**SmartAccountTransfer**](SmartAccountTransfer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve |  -  |
**404** | Smart account not found |  -  |
**400** | Smart account insufficient balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_account_transfer_create**
> SmartAccountTransfer smart_account_transfer_create(id, create_smart_account_transfer_request)

Create Transfer

Creates the smart account transfer resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_smart_account_transfer_request import CreateSmartAccountTransferRequest
from pluggy_sdk.models.smart_account_transfer import SmartAccountTransfer
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
    api_instance = pluggy_sdk.SmartAccountTransferApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Smart account primary identifier
    create_smart_account_transfer_request = pluggy_sdk.CreateSmartAccountTransferRequest() # CreateSmartAccountTransferRequest | 

    try:
        # Create Transfer
        api_response = api_instance.smart_account_transfer_create(id, create_smart_account_transfer_request)
        print("The response of SmartAccountTransferApi->smart_account_transfer_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartAccountTransferApi->smart_account_transfer_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Smart account primary identifier | 
 **create_smart_account_transfer_request** | [**CreateSmartAccountTransferRequest**](CreateSmartAccountTransferRequest.md)|  | 

### Return type

[**SmartAccountTransfer**](SmartAccountTransfer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a transfer. |  -  |
**400** | Smart account transfer is Invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

