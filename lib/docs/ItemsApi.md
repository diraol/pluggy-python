# openapi_client.ItemsApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_create**](ItemsApi.md#items_create) | **POST** /items | Create
[**items_delete**](ItemsApi.md#items_delete) | **DELETE** /items/{id} | Delete
[**items_retrieve**](ItemsApi.md#items_retrieve) | **GET** /items/{id} | Retrieve
[**items_send_mfa**](ItemsApi.md#items_send_mfa) | **POST** /items/{id}/mfa | Send MFA
[**items_update**](ItemsApi.md#items_update) | **PATCH** /items/{id} | Update


# **items_create**
> Item items_create(create_item)

Create

Creates a item and syncs all the products with the financial institution, using as credentials the sent parameters.

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.create_item import CreateItem
from openapi_client.models.item import Item
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
    api_instance = openapi_client.ItemsApi(api_client)
    create_item = {"connectorId":2,"parameters":{"user":"user-ok","password":"password-ok"},"webhookUrl":"https://example.com/webhook"} # CreateItem | 

    try:
        # Create
        api_response = api_instance.items_create(create_item)
        print("The response of ItemsApi->items_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_item** | [**CreateItem**](CreateItem.md)|  | 

### Return type

[**Item**](Item.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created item |  -  |
**400** | Invalid parameters |  -  |
**409** | There is a conflict creating an item |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_delete**
> ICountResponse items_delete(id)

Delete

Delete the item by its primary identifier

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.i_count_response import ICountResponse
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
    api_instance = openapi_client.ItemsApi(api_client)
    id = 'd0f8a8c0-e8e3-11e9-b210-d663bd873d93' # str | Item primary identifier

    try:
        # Delete
        api_response = api_instance.items_delete(id)
        print("The response of ItemsApi->items_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item primary identifier | 

### Return type

[**ICountResponse**](ICountResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item was deleted |  -  |
**404** | Item not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_retrieve**
> Item items_retrieve(id)

Retrieve

Recovers the item resource by its id

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.item import Item
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
    api_instance = openapi_client.ItemsApi(api_client)
    id = 'd0f8a8c0-e8e3-11e9-b210-d663bd873d93' # str | Item primary identifier

    try:
        # Retrieve
        api_response = api_instance.items_retrieve(id)
        print("The response of ItemsApi->items_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item primary identifier | 

### Return type

[**Item**](Item.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item was retrieved |  -  |
**404** | Item not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_send_mfa**
> Item items_send_mfa(id, request_body)

Send MFA

When item is Waiting User Input, this method allows to submit multi-factor authentication value

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.item import Item
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
    api_instance = openapi_client.ItemsApi(api_client)
    id = 'd0e8448e-0156-4b4a-ae6c-3e2a6d9bff5c' # str | Item primary identifier
    request_body = {'key': 'request_body_example'} # Dict[str, str] | 

    try:
        # Send MFA
        api_response = api_instance.items_send_mfa(id, request_body)
        print("The response of ItemsApi->items_send_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_send_mfa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item primary identifier | 
 **request_body** | [**Dict[str, str]**](str.md)|  | 

### Return type

[**Item**](Item.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parameter was sent correctly |  -  |
**404** | Item not found |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_update**
> Item items_update(id, update_item=update_item)

Update

Triggers new syncronization for the Item, optionally updating the stored credentials.

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.item import Item
from openapi_client.models.update_item import UpdateItem
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
    api_instance = openapi_client.ItemsApi(api_client)
    id = 'd0f8a8c0-e8e3-11e9-b210-d663bd873d93' # str | Item primary identifier
    update_item = {"webhookUrl":"https://example.com/webhook","clientUserId":"My User App Id","parameters":{"user":"user-ok","password":"password-ok"}} # UpdateItem | Update item request (optional)

    try:
        # Update
        api_response = api_instance.items_update(id, update_item=update_item)
        print("The response of ItemsApi->items_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item primary identifier | 
 **update_item** | [**UpdateItem**](UpdateItem.md)| Update item request | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the item was successful, new sync was triggered |  -  |
**400** | Invalid parameters |  -  |
**404** | Item not found |  -  |
**409** | There is a conflict updating the item |  -  |
**500** | Server Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

