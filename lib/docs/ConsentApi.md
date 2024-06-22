# pluggy_sdk.ConsentApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consent_retrieve**](ConsentApi.md#consent_retrieve) | **GET** /consents/{id} | Retrieve
[**consents_list**](ConsentApi.md#consents_list) | **GET** /consents | List


# **consent_retrieve**
> Consent consent_retrieve(id)

Retrieve

Recovers the consent resource by it's id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.consent import Consent
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
    api_instance = pluggy_sdk.ConsentApi(api_client)
    id = '6ec156fe-e8ac-4d9a-a4b3-7770529ab01c' # str | Consent primary identifier

    try:
        # Retrieve
        api_response = api_instance.consent_retrieve(id)
        print("The response of ConsentApi->consent_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsentApi->consent_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Consent primary identifier | 

### Return type

[**Consent**](Consent.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a consent. |  -  |
**404** | Consent not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consents_list**
> PageResponseConsents consents_list(item_id)

List

Recovers all consents given to the item provided

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.page_response_consents import PageResponseConsents
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
    api_instance = pluggy_sdk.ConsentApi(api_client)
    item_id = 'd0f8a8c0-e8e3-11e9-b210-d663bd873d93' # str | Item primary identifier

    try:
        # List
        api_response = api_instance.consents_list(item_id)
        print("The response of ConsentApi->consents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsentApi->consents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item primary identifier | 

### Return type

[**PageResponseConsents**](PageResponseConsents.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all consents given to an item |  -  |
**400** | Missing parameter |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

