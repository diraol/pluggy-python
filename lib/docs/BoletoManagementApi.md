# pluggy_sdk.BoletoManagementApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boleto_cancel**](BoletoManagementApi.md#boleto_cancel) | **POST** /boletos/{id}/cancel | Cancel Boleto
[**boleto_connection_create**](BoletoManagementApi.md#boleto_connection_create) | **POST** /boleto-connections | Connect boleto credentials
[**boleto_create**](BoletoManagementApi.md#boleto_create) | **POST** /boletos | Issue Boleto


# **boleto_cancel**
> IssuedBoleto boleto_cancel(id)

Cancel Boleto

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.issued_boleto import IssuedBoleto
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
    api_instance = pluggy_sdk.BoletoManagementApi(api_client)
    id = '82da0d63-fbc0-4e20-b191-50e6df030875' # str | Boleto primary identifier

    try:
        # Cancel Boleto
        api_response = api_instance.boleto_cancel(id)
        print("The response of BoletoManagementApi->boleto_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoletoManagementApi->boleto_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Boleto primary identifier | 

### Return type

[**IssuedBoleto**](IssuedBoleto.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boleto cancelled successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boleto_connection_create**
> BoletoConnection boleto_connection_create(create_boleto_connection)

Connect boleto credentials

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.boleto_connection import BoletoConnection
from pluggy_sdk.models.create_boleto_connection import CreateBoletoConnection
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
    api_instance = pluggy_sdk.BoletoManagementApi(api_client)
    create_boleto_connection = pluggy_sdk.CreateBoletoConnection() # CreateBoletoConnection | 

    try:
        # Connect boleto credentials
        api_response = api_instance.boleto_connection_create(create_boleto_connection)
        print("The response of BoletoManagementApi->boleto_connection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoletoManagementApi->boleto_connection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_boleto_connection** | [**CreateBoletoConnection**](CreateBoletoConnection.md)|  | 

### Return type

[**BoletoConnection**](BoletoConnection.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boleto connection created successfully |  -  |
**400** | Incorrect credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boleto_create**
> IssuedBoleto boleto_create(create_boleto)

Issue Boleto

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_boleto import CreateBoleto
from pluggy_sdk.models.issued_boleto import IssuedBoleto
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
    api_instance = pluggy_sdk.BoletoManagementApi(api_client)
    create_boleto = pluggy_sdk.CreateBoleto() # CreateBoleto | 

    try:
        # Issue Boleto
        api_response = api_instance.boleto_create(create_boleto)
        print("The response of BoletoManagementApi->boleto_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoletoManagementApi->boleto_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_boleto** | [**CreateBoleto**](CreateBoleto.md)|  | 

### Return type

[**IssuedBoleto**](IssuedBoleto.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boleto created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

