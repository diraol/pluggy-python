# pluggy_sdk.WebhookApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_create**](WebhookApi.md#webhooks_create) | **POST** /webhooks | Create
[**webhooks_delete**](WebhookApi.md#webhooks_delete) | **DELETE** /webhooks/{id} | Delete
[**webhooks_list**](WebhookApi.md#webhooks_list) | **GET** /webhooks | List
[**webhooks_retrieve**](WebhookApi.md#webhooks_retrieve) | **GET** /webhooks/{id} | Retrieve
[**webhooks_update**](WebhookApi.md#webhooks_update) | **PATCH** /webhooks/{id} | Update


# **webhooks_create**
> Webhook webhooks_create(create_webhook)

Create

Creates a webhook attached to the specific event and provides the notification url

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_webhook import CreateWebhook
from pluggy_sdk.models.webhook import Webhook
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
    api_instance = pluggy_sdk.WebhookApi(api_client)
    create_webhook = pluggy_sdk.CreateWebhook() # CreateWebhook | Expects the following webhooks parameters: event: One of the event types that are supported. url: An https url that will receive the POST of the event. headers: optional key-value pairs to send with the POST of the event.

    try:
        # Create
        api_response = api_instance.webhooks_create(create_webhook)
        print("The response of WebhookApi->webhooks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook** | [**CreateWebhook**](CreateWebhook.md)| Expects the following webhooks parameters: event: One of the event types that are supported. url: An https url that will receive the POST of the event. headers: optional key-value pairs to send with the POST of the event. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created webhook |  -  |
**400** | Invalid parameters |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_delete**
> ICountResponse webhooks_delete(id)

Delete

Deletes a webhook listener by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.i_count_response import ICountResponse
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
    api_instance = pluggy_sdk.WebhookApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | webhook primary identifier

    try:
        # Delete
        api_response = api_instance.webhooks_delete(id)
        print("The response of WebhookApi->webhooks_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| webhook primary identifier | 

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
**200** | Webhook was deleted |  -  |
**404** | Webhook not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_list**
> WebhooksList200Response webhooks_list()

List

Retrieves all Webhooks associated with your application

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.webhooks_list200_response import WebhooksList200Response
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
    api_instance = pluggy_sdk.WebhookApi(api_client)

    try:
        # List
        api_response = api_instance.webhooks_list()
        print("The response of WebhookApi->webhooks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhooksList200Response**](WebhooksList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Webhooks |  -  |
**500** | Unexpected error |  -  |
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_retrieve**
> Webhook webhooks_retrieve(id)

Retrieve

Retrieves a specific webhook

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.webhook import Webhook
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
    api_instance = pluggy_sdk.WebhookApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | webhook primary identifier

    try:
        # Retrieve
        api_response = api_instance.webhooks_retrieve(id)
        print("The response of WebhookApi->webhooks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| webhook primary identifier | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a webhook. |  -  |
**404** | Webhook not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_update**
> Webhook webhooks_update(id, create_webhook)

Update

Updates a webhook event and/or url listener. Once updated all events that are triggered will replicate the updated logic

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_webhook import CreateWebhook
from pluggy_sdk.models.webhook import Webhook
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
    api_instance = pluggy_sdk.WebhookApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | webhook primary identifier
    create_webhook = pluggy_sdk.CreateWebhook() # CreateWebhook | Expects the following webhooks parameters: event: One of the event types that are supported. url: An https url that will receive the POST of the event. headers: optional key-value pairs to send with the POST of the event.

    try:
        # Update
        api_response = api_instance.webhooks_update(id, create_webhook)
        print("The response of WebhookApi->webhooks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| webhook primary identifier | 
 **create_webhook** | [**CreateWebhook**](CreateWebhook.md)| Expects the following webhooks parameters: event: One of the event types that are supported. url: An https url that will receive the POST of the event. headers: optional key-value pairs to send with the POST of the event. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the webhook that was sent |  -  |
**400** | Invalid parameters |  -  |
**404** | Webhook not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

