# pluggy_sdk.PaymentRecipientApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_recipient_create**](PaymentRecipientApi.md#payment_recipient_create) | **POST** /payments/recipients | Create
[**payment_recipient_delete**](PaymentRecipientApi.md#payment_recipient_delete) | **DELETE** /payments/recipients/{id} | Delete
[**payment_recipient_institutions_retrieve**](PaymentRecipientApi.md#payment_recipient_institutions_retrieve) | **GET** /payments/recipients/institutions/{id} | Retrieve Institution
[**payment_recipient_retrieve**](PaymentRecipientApi.md#payment_recipient_retrieve) | **GET** /payments/recipients/{id} | Retrieve
[**payment_recipient_update**](PaymentRecipientApi.md#payment_recipient_update) | **PATCH** /payments/recipients/{id} | Update
[**payment_recipients_institution_list**](PaymentRecipientApi.md#payment_recipients_institution_list) | **GET** /payments/recipients/institutions | List Institutions
[**payment_recipients_list**](PaymentRecipientApi.md#payment_recipients_list) | **GET** /payments/recipients | List


# **payment_recipient_create**
> PaymentRecipient payment_recipient_create(create_payment_recipient)

Create

Creates the payment recipient resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_payment_recipient import CreatePaymentRecipient
from pluggy_sdk.models.payment_recipient import PaymentRecipient
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
    api_instance = pluggy_sdk.PaymentRecipientApi(api_client)
    create_payment_recipient = pluggy_sdk.CreatePaymentRecipient() # CreatePaymentRecipient | 

    try:
        # Create
        api_response = api_instance.payment_recipient_create(create_payment_recipient)
        print("The response of PaymentRecipientApi->payment_recipient_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRecipientApi->payment_recipient_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_recipient** | [**CreatePaymentRecipient**](CreatePaymentRecipient.md)|  | 

### Return type

[**PaymentRecipient**](PaymentRecipient.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a payment recipient. |  -  |
**400** | Payment Recipient its Invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_recipient_delete**
> payment_recipient_delete(id)

Delete

Deletes the payment recipient resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
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
    api_instance = pluggy_sdk.PaymentRecipientApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment recipient primary identifier

    try:
        # Delete
        api_instance.payment_recipient_delete(id)
    except Exception as e:
        print("Exception when calling PaymentRecipientApi->payment_recipient_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment recipient primary identifier | 

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a recipient. |  -  |
**404** | Payment recipient not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_recipient_institutions_retrieve**
> PaymentInstitution payment_recipient_institutions_retrieve(id)

Retrieve Institution

Recovers the payment institution resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_institution import PaymentInstitution
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
    api_instance = pluggy_sdk.PaymentRecipientApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment institution primary identifier

    try:
        # Retrieve Institution
        api_response = api_instance.payment_recipient_institutions_retrieve(id)
        print("The response of PaymentRecipientApi->payment_recipient_institutions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRecipientApi->payment_recipient_institutions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment institution primary identifier | 

### Return type

[**PaymentInstitution**](PaymentInstitution.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a payment institution. |  -  |
**404** | Payment Institution not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_recipient_retrieve**
> PaymentRecipient payment_recipient_retrieve(id)

Retrieve

Recovers the payment recipient resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_recipient import PaymentRecipient
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
    api_instance = pluggy_sdk.PaymentRecipientApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment recipient primary identifier

    try:
        # Retrieve
        api_response = api_instance.payment_recipient_retrieve(id)
        print("The response of PaymentRecipientApi->payment_recipient_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRecipientApi->payment_recipient_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment recipient primary identifier | 

### Return type

[**PaymentRecipient**](PaymentRecipient.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a recipient. |  -  |
**404** | Payment Recipient not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_recipient_update**
> PaymentRecipient payment_recipient_update(id, update_payment_recipient)

Update

Updates the payment recipient resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_recipient import PaymentRecipient
from pluggy_sdk.models.update_payment_recipient import UpdatePaymentRecipient
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
    api_instance = pluggy_sdk.PaymentRecipientApi(api_client)
    id = 'd0f8a8c0-e8e3-11e9-b210-d663bd873d93' # str | Payment recipient primary identifier
    update_payment_recipient = pluggy_sdk.UpdatePaymentRecipient() # UpdatePaymentRecipient | 

    try:
        # Update
        api_response = api_instance.payment_recipient_update(id, update_payment_recipient)
        print("The response of PaymentRecipientApi->payment_recipient_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRecipientApi->payment_recipient_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment recipient primary identifier | 
 **update_payment_recipient** | [**UpdatePaymentRecipient**](UpdatePaymentRecipient.md)|  | 

### Return type

[**PaymentRecipient**](PaymentRecipient.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a payment recipient. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_recipients_institution_list**
> PaymentRecipientsInstitutionList200Response payment_recipients_institution_list(page_size=page_size, page=page, name=name)

List Institutions

Recovers all created payment institutions

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_recipients_institution_list200_response import PaymentRecipientsInstitutionList200Response
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
    api_instance = pluggy_sdk.PaymentRecipientApi(api_client)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)
    name = 'Itau' # str | Filter institutions by name (optional)

    try:
        # List Institutions
        api_response = api_instance.payment_recipients_institution_list(page_size=page_size, page=page, name=name)
        print("The response of PaymentRecipientApi->payment_recipients_institution_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRecipientApi->payment_recipients_institution_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 
 **name** | **str**| Filter institutions by name | [optional] 

### Return type

[**PaymentRecipientsInstitutionList200Response**](PaymentRecipientsInstitutionList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all payment institutions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_recipients_list**
> PaymentRecipientsList200Response payment_recipients_list(is_default=is_default, page_size=page_size, page=page)

List

Recovers all created payment recipients

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_recipients_list200_response import PaymentRecipientsList200Response
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
    api_instance = pluggy_sdk.PaymentRecipientApi(api_client)
    is_default = true # bool | Filter recipients only if its default or not (optional)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)

    try:
        # List
        api_response = api_instance.payment_recipients_list(is_default=is_default, page_size=page_size, page=page)
        print("The response of PaymentRecipientApi->payment_recipients_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRecipientApi->payment_recipients_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_default** | **bool**| Filter recipients only if its default or not | [optional] 
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 

### Return type

[**PaymentRecipientsList200Response**](PaymentRecipientsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all payment recipients |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

