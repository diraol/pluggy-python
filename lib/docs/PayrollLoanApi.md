# pluggy_sdk.PayrollLoanApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payroll_loans_list**](PayrollLoanApi.md#payroll_loans_list) | **GET** /payroll-loans | List
[**payroll_loans_retrieve**](PayrollLoanApi.md#payroll_loans_retrieve) | **GET** /payroll-loans/{id} | Retrieve


# **payroll_loans_list**
> PayrollLoansList200Response payroll_loans_list(item_id)

List

Recovers all payroll loans collected for the item provided

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payroll_loans_list200_response import PayrollLoansList200Response
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
    api_instance = pluggy_sdk.PayrollLoanApi(api_client)
    item_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Item's primary identifier

    try:
        # List
        api_response = api_instance.payroll_loans_list(item_id)
        print("The response of PayrollLoanApi->payroll_loans_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollLoanApi->payroll_loans_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item&#39;s primary identifier | 

### Return type

[**PayrollLoansList200Response**](PayrollLoansList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all payroll loans |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payroll_loans_retrieve**
> PayrollLoanResponse payroll_loans_retrieve(id)

Retrieve

Recovers the payroll loan resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.payroll_loan_response import PayrollLoanResponse
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
    api_instance = pluggy_sdk.PayrollLoanApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | loan primary identifier

    try:
        # Retrieve
        api_response = api_instance.payroll_loans_retrieve(id)
        print("The response of PayrollLoanApi->payroll_loans_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollLoanApi->payroll_loans_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| loan primary identifier | 

### Return type

[**PayrollLoanResponse**](PayrollLoanResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a payroll loan. |  -  |
**404** | PayrollLoan not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

