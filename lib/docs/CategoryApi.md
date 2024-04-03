# openapi_client.CategoryApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_list**](CategoryApi.md#categories_list) | **GET** /categories | List
[**categories_retrieve**](CategoryApi.md#categories_retrieve) | **GET** /categories/{id} | Retrieve
[**client_category_rules_create**](CategoryApi.md#client_category_rules_create) | **POST** /categories/rules | Create Category Rule
[**client_category_rules_list**](CategoryApi.md#client_category_rules_list) | **GET** /categories/rules | List Category Rules


# **categories_list**
> List[Category] categories_list(parent_id=parent_id)

List

Recovers all categories active from the data categorization. Can be filtered by the parentId of the category.

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.category import Category
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
    api_instance = openapi_client.CategoryApi(api_client)
    parent_id = '01000000' # str | Parent's primary identifier (optional)

    try:
        # List
        api_response = api_instance.categories_list(parent_id=parent_id)
        print("The response of CategoryApi->categories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->categories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**| Parent&#39;s primary identifier | [optional] 

### Return type

[**List[Category]**](Category.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all categories |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_retrieve**
> Category categories_retrieve(id)

Retrieve

Recovers the category resource by its id

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.category import Category
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
    api_instance = openapi_client.CategoryApi(api_client)
    id = '01000000' # str | category primary identifier

    try:
        # Retrieve
        api_response = api_instance.categories_retrieve(id)
        print("The response of CategoryApi->categories_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->categories_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| category primary identifier | 

### Return type

[**Category**](Category.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a category. |  -  |
**404** | Category not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_category_rules_create**
> ClientCategoryRule client_category_rules_create(create_client_category_rule)

Create Category Rule

Create a single category rule

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.client_category_rule import ClientCategoryRule
from openapi_client.models.create_client_category_rule import CreateClientCategoryRule
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
    api_instance = openapi_client.CategoryApi(api_client)
    create_client_category_rule = openapi_client.CreateClientCategoryRule() # CreateClientCategoryRule | 

    try:
        # Create Category Rule
        api_response = api_instance.client_category_rules_create(create_client_category_rule)
        print("The response of CategoryApi->client_category_rules_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->client_category_rules_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client_category_rule** | [**CreateClientCategoryRule**](CreateClientCategoryRule.md)|  | 

### Return type

[**ClientCategoryRule**](ClientCategoryRule.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creates a Category Rule and recover the result |  -  |
**404** | Category not found |  -  |
**400** | Invalid description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_category_rules_list**
> List[PageResponseCategoryRules] client_category_rules_list()

List Category Rules

Recovers category rules

### Example

* Api Key Authentication (default):

```python
import openapi_client
from openapi_client.models.page_response_category_rules import PageResponseCategoryRules
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
    api_instance = openapi_client.CategoryApi(api_client)

    try:
        # List Category Rules
        api_response = api_instance.client_category_rules_list()
        print("The response of CategoryApi->client_category_rules_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->client_category_rules_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PageResponseCategoryRules]**](PageResponseCategoryRules.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all client category rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

