# openapi_client.ConnectorApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connector_retrieve**](ConnectorApi.md#connector_retrieve) | **GET** /connectors/{id} | Retrieve
[**connectors_list**](ConnectorApi.md#connectors_list) | **GET** /connectors | List
[**connectors_validate**](ConnectorApi.md#connectors_validate) | **POST** /connectors/{id}/validate | Validate


# **connector_retrieve**
> Connector connector_retrieve(id, health_details=health_details)

Retrieve

This endpoint retrieves a specific connector.

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.connector import Connector
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
    api_instance = openapi_client.ConnectorApi(api_client)
    id = 201 # float | Connector primary identifier
    health_details = True # bool | Include health details about latest connections and percentage of errors (connection rate) (optional)

    try:
        # Retrieve
        api_response = api_instance.connector_retrieve(id, health_details=health_details)
        print("The response of ConnectorApi->connector_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->connector_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Connector primary identifier | 
 **health_details** | **bool**| Include health details about latest connections and percentage of errors (connection rate) | [optional] 

### Return type

[**Connector**](Connector.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a connector. |  -  |
**404** | Connector not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_list**
> ConnectorListResponse connectors_list(countries=countries, types=types, name=name, sandbox=sandbox, health_details=health_details, is_open_finance=is_open_finance, supports_payment_initiation=supports_payment_initiation)

List

This endpoint retrieves all available connectors.

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.connector_list_response import ConnectorListResponse
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
    api_instance = openapi_client.ConnectorApi(api_client)
    countries = ['[\"BR\"]'] # List[str] | A list of countries of connectors to filter. (optional)
    types = ['[\"PERSONAL_BANK\", \"BUSINESS_BANK\", \"INVESTMENT\", \"INVOICE\", \"TELECOMMUNICATION\", \"OTHER\"]'] # List[str] | A list of types of connectors to filter. (optional)
    name = 'name_example' # str | Name alike look up of the connector (optional)
    sandbox = True # bool | Include sandbox connectors if set to true (default: false). (optional)
    health_details = True # bool | Include health details about latest connections and percentage of errors (connection rate) (optional)
    is_open_finance = True # bool | Filter connectors by the `isOpenFinance` attribute. If not sent, it won't filter. (optional)
    supports_payment_initiation = True # bool | Filter connectors by the `supportsPaymentInitiation` attribute. If not sent, it won't filter. (optional)

    try:
        # List
        api_response = api_instance.connectors_list(countries=countries, types=types, name=name, sandbox=sandbox, health_details=health_details, is_open_finance=is_open_finance, supports_payment_initiation=supports_payment_initiation)
        print("The response of ConnectorApi->connectors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->connectors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | [**List[str]**](str.md)| A list of countries of connectors to filter. | [optional] 
 **types** | [**List[str]**](str.md)| A list of types of connectors to filter. | [optional] 
 **name** | **str**| Name alike look up of the connector | [optional] 
 **sandbox** | **bool**| Include sandbox connectors if set to true (default: false). | [optional] 
 **health_details** | **bool**| Include health details about latest connections and percentage of errors (connection rate) | [optional] 
 **is_open_finance** | **bool**| Filter connectors by the &#x60;isOpenFinance&#x60; attribute. If not sent, it won&#39;t filter. | [optional] 
 **supports_payment_initiation** | **bool**| Filter connectors by the &#x60;supportsPaymentInitiation&#x60; attribute. If not sent, it won&#39;t filter. | [optional] 

### Return type

[**ConnectorListResponse**](ConnectorListResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all connectors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_validate**
> ParameterValidationResponse connectors_validate(id, request_body)

Validate

Validates a connector parameters usign the connector validation

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.parameter_validation_response import ParameterValidationResponse
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
    api_instance = openapi_client.ConnectorApi(api_client)
    id = 2 # float | Connector's primary identifier
    request_body = {'key': 'request_body_example'} # Dict[str, str] | Connector's input credentials in a key-value object.

    try:
        # Validate
        api_response = api_instance.connectors_validate(id, request_body)
        print("The response of ConnectorApi->connectors_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->connectors_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Connector&#39;s primary identifier | 
 **request_body** | [**Dict[str, str]**](str.md)| Connector&#39;s input credentials in a key-value object. | 

### Return type

[**ParameterValidationResponse**](ParameterValidationResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector validation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

