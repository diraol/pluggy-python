# pluggy_sdk.PaymentCustomerApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_customer_create**](PaymentCustomerApi.md#payment_customer_create) | **POST** /payments/customers | Create
[**payment_customer_delete**](PaymentCustomerApi.md#payment_customer_delete) | **DELETE** /payments/customers/{id} | Delete
[**payment_customer_retrieve**](PaymentCustomerApi.md#payment_customer_retrieve) | **GET** /payments/customers/{id} | Retrieve
[**payment_customer_update**](PaymentCustomerApi.md#payment_customer_update) | **PATCH** /payments/customers/{id} | Update
[**payment_customers_list**](PaymentCustomerApi.md#payment_customers_list) | **GET** /payments/customers | List


# **payment_customer_create**
> PaymentCustomer payment_customer_create(create_payment_customer_request_body)

Create

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_payment_customer_request_body import CreatePaymentCustomerRequestBody
from pluggy_sdk.models.payment_customer import PaymentCustomer
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
    api_instance = pluggy_sdk.PaymentCustomerApi(api_client)
    create_payment_customer_request_body = pluggy_sdk.CreatePaymentCustomerRequestBody() # CreatePaymentCustomerRequestBody | 

    try:
        # Create
        api_response = api_instance.payment_customer_create(create_payment_customer_request_body)
        print("The response of PaymentCustomerApi->payment_customer_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentCustomerApi->payment_customer_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_customer_request_body** | [**CreatePaymentCustomerRequestBody**](CreatePaymentCustomerRequestBody.md)|  | 

### Return type

[**PaymentCustomer**](PaymentCustomer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a payment customer. |  -  |
**400** | Payment Customer its Invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_customer_delete**
> payment_customer_delete(id)

Delete

Deletes the payment customer resource by its id

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
    api_instance = pluggy_sdk.PaymentCustomerApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment customer primary identifier

    try:
        # Delete
        api_instance.payment_customer_delete(id)
    except Exception as e:
        print("Exception when calling PaymentCustomerApi->payment_customer_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment customer primary identifier | 

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
**200** | Delete a customer request. |  -  |
**404** | Payment customer not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_customer_retrieve**
> PaymentCustomer payment_customer_retrieve(id)

Retrieve

Recovers the payment customer resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_customer import PaymentCustomer
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
    api_instance = pluggy_sdk.PaymentCustomerApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Payment customer primary identifier

    try:
        # Retrieve
        api_response = api_instance.payment_customer_retrieve(id)
        print("The response of PaymentCustomerApi->payment_customer_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentCustomerApi->payment_customer_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment customer primary identifier | 

### Return type

[**PaymentCustomer**](PaymentCustomer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a customer request. |  -  |
**404** | Payment Customer not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_customer_update**
> PaymentCustomer payment_customer_update(id, create_or_update_payment_customer)

Update

Updates the payment customer resource

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_or_update_payment_customer import CreateOrUpdatePaymentCustomer
from pluggy_sdk.models.payment_customer import PaymentCustomer
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
    api_instance = pluggy_sdk.PaymentCustomerApi(api_client)
    id = 'd0f8a8c0-e8e3-11e9-b210-d663bd873d93' # str | Payment customer primary identifier
    create_or_update_payment_customer = pluggy_sdk.CreateOrUpdatePaymentCustomer() # CreateOrUpdatePaymentCustomer | 

    try:
        # Update
        api_response = api_instance.payment_customer_update(id, create_or_update_payment_customer)
        print("The response of PaymentCustomerApi->payment_customer_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentCustomerApi->payment_customer_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment customer primary identifier | 
 **create_or_update_payment_customer** | [**CreateOrUpdatePaymentCustomer**](CreateOrUpdatePaymentCustomer.md)|  | 

### Return type

[**PaymentCustomer**](PaymentCustomer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a payment customer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_customers_list**
> PaymentCustomersList200Response payment_customers_list(page_size=page_size, page=page, name=name, email=email, cpf=cpf, cnpj=cnpj)

List

Recovers all created payment customers

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payment_customers_list200_response import PaymentCustomersList200Response
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
    api_instance = pluggy_sdk.PaymentCustomerApi(api_client)
    page_size = 50 # float | Page size for the paging request, default: 20 (optional)
    page = 1 # float | Page number for the paging request, default: 1 (optional)
    name = 'John' # str | Filter payment customers by name (optional)
    email = 'john.doe@email.com' # str | Filter payment customers by email (optional)
    cpf = '11111111111' # str | Filter payment customers by CPF (optional)
    cnpj = '1111111111111' # str | Filter payment customers by CNPJ (optional)

    try:
        # List
        api_response = api_instance.payment_customers_list(page_size=page_size, page=page, name=name, email=email, cpf=cpf, cnpj=cnpj)
        print("The response of PaymentCustomerApi->payment_customers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentCustomerApi->payment_customers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| Page size for the paging request, default: 20 | [optional] 
 **page** | **float**| Page number for the paging request, default: 1 | [optional] 
 **name** | **str**| Filter payment customers by name | [optional] 
 **email** | **str**| Filter payment customers by email | [optional] 
 **cpf** | **str**| Filter payment customers by CPF | [optional] 
 **cnpj** | **str**| Filter payment customers by CNPJ | [optional] 

### Return type

[**PaymentCustomersList200Response**](PaymentCustomersList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all payment customers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

