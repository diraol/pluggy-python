# pluggy_sdk.BenefitApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**benefit_retrieve_by_id**](BenefitApi.md#benefit_retrieve_by_id) | **GET** /benefits/{id} | Retrieve
[**benefits_list**](BenefitApi.md#benefits_list) | **GET** /benefits | List


# **benefit_retrieve_by_id**
> BenefitResponse benefit_retrieve_by_id(id)

Retrieve

Recovers the benefit resource by its id

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.benefit_response import BenefitResponse
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
    api_instance = pluggy_sdk.BenefitApi(api_client)
    id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | benefit primary identifier

    try:
        # Retrieve
        api_response = api_instance.benefit_retrieve_by_id(id)
        print("The response of BenefitApi->benefit_retrieve_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitApi->benefit_retrieve_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| benefit primary identifier | 

### Return type

[**BenefitResponse**](BenefitResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a benefit by it&#39;s id. |  -  |
**404** | Benefit not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **benefits_list**
> BenefitsList200Response benefits_list(item_id)

List

Recovers all benefits collected for the item provided

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.benefits_list200_response import BenefitsList200Response
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
    api_instance = pluggy_sdk.BenefitApi(api_client)
    item_id = 'd0e8a7f0-6d86-11ea-b77f-2e728ce88125' # str | Item's primary identifier

    try:
        # List
        api_response = api_instance.benefits_list(item_id)
        print("The response of BenefitApi->benefits_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitApi->benefits_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item&#39;s primary identifier | 

### Return type

[**BenefitsList200Response**](BenefitsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a list of all benefits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

