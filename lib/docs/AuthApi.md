# pluggy_sdk.AuthApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_create**](AuthApi.md#auth_create) | **POST** /auth | Create API Key
[**connect_token_create**](AuthApi.md#connect_token_create) | **POST** /connect_token | Create Connect Token


# **auth_create**
> AuthResponse auth_create(auth_request)

Create API Key

Validate clientId and clientSecret and return an API Key

### Example


```python
import pluggy_sdk
from pluggy_sdk.models.auth_request import AuthRequest
from pluggy_sdk.models.auth_response import AuthResponse
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
    api_instance = pluggy_sdk.AuthApi(api_client)
    auth_request = pluggy_sdk.AuthRequest() # AuthRequest | 

    try:
        # Create API Key
        api_response = api_instance.auth_create(auth_request)
        print("The response of AuthApi->auth_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API Key generated |  -  |
**401** | Invalid credentials |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_token_create**
> ConnectTokenResponse connect_token_create(connect_token_request=connect_token_request)

Create Connect Token

Creates a connect token

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.connect_token_request import ConnectTokenRequest
from pluggy_sdk.models.connect_token_response import ConnectTokenResponse
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
    api_instance = pluggy_sdk.AuthApi(api_client)
    connect_token_request = pluggy_sdk.ConnectTokenRequest() # ConnectTokenRequest | Create connect token payload (optional)

    try:
        # Create Connect Token
        api_response = api_instance.connect_token_create(connect_token_request=connect_token_request)
        print("The response of AuthApi->connect_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->connect_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_token_request** | [**ConnectTokenRequest**](ConnectTokenRequest.md)| Create connect token payload | [optional] 

### Return type

[**ConnectTokenResponse**](ConnectTokenResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created connect token |  -  |
**403** | Unauthenticated |  -  |
**404** | Related itemId to update not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

