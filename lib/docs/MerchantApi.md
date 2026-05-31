# pluggy_sdk.MerchantApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchants_get_by_cnpj**](MerchantApi.md#merchants_get_by_cnpj) | **GET** /merchants | Get merchants by CNPJ list


# **merchants_get_by_cnpj**
> MerchantsGetByCnpj200Response merchants_get_by_cnpj(cnpjs=cnpjs)

Get merchants by CNPJ list

Retrieves merchant information for a list of CNPJs. Returns an object containing found merchants, valid CNPJs that were not found, and invalid CNPJs.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.merchants_get_by_cnpj200_response import MerchantsGetByCnpj200Response
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
    api_instance = pluggy_sdk.MerchantApi(api_client)
    cnpjs = '00000000000191,60701190000104' # str | Comma-separated list of CNPJs (optional)

    try:
        # Get merchants by CNPJ list
        api_response = api_instance.merchants_get_by_cnpj(cnpjs=cnpjs)
        print("The response of MerchantApi->merchants_get_by_cnpj:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->merchants_get_by_cnpj: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cnpjs** | **str**| Comma-separated list of CNPJs | [optional] 

### Return type

[**MerchantsGetByCnpj200Response**](MerchantsGetByCnpj200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Merchant query results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

