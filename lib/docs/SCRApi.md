# pluggy_sdk.SCRApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_retrieve_scr**](SCRApi.md#items_retrieve_scr) | **GET** /items/{id}/scr | Retrieve SCR


# **items_retrieve_scr**
> ScrResponse items_retrieve_scr(id, var_from=var_from, to=to)

Retrieve SCR

Retrieves the SCR (Bacen's *Sistema de Informações de Crédito*) for the document behind a connected item.

The SCR is the Banco Central's official registry of credit operations: every loan, financing, limit and guarantee above R$200, reported by every financial institution. The response is Bacen's own payload, forwarded unchanged.

The item is not the source of the data — the SCR is keyed by the document alone. The item supplies the CPF/CNPJ and stands as the evidence of the account holder's consent, which is why this is only available for Open Finance items whose document is known.

Requires the SCR feature on your subscription. Talk to us if you want it enabled.

Base dates are months, not days, and Bacen consolidates each one with a few months of delay. When `from` and `to` are omitted the last 4 available base dates are consulted, ending 2 months back from today — asking for the current month returns nothing, because Bacen has not closed it yet.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.scr_response import ScrResponse
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
    api_instance = pluggy_sdk.SCRApi(api_client)
    id = UUID('d0e8448e-0156-4b4a-ae6c-3e2a6d9bff5c') # UUID | Item primary identifier
    var_from = '202604' # str | First base date to consult, as YYYYMM. Defaults to 3 base dates before `to` (optional)
    to = '202607' # str | Last base date to consult, as YYYYMM. Defaults to 2 months before the current one, which is the most recent base date Bacen has consolidated (optional)

    try:
        # Retrieve SCR
        api_response = api_instance.items_retrieve_scr(id, var_from=var_from, to=to)
        print("The response of SCRApi->items_retrieve_scr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCRApi->items_retrieve_scr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Item primary identifier | 
 **var_from** | **str**| First base date to consult, as YYYYMM. Defaults to 3 base dates before &#x60;to&#x60; | [optional] 
 **to** | **str**| Last base date to consult, as YYYYMM. Defaults to 2 months before the current one, which is the most recent base date Bacen has consolidated | [optional] 

### Return type

[**ScrResponse**](ScrResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SCR data for the item document |  -  |
**400** | The SCR request was rejected as invalid. Check the databaseIni/databaseFim range. |  -  |
**403** | This client is not enabled to query SCR data. |  -  |
**404** | item not found |  -  |
**422** | SCR is only available for Open Finance items that have a known CPF or CNPJ. |  -  |
**500** | An error occurred while fetching the SCR data from the connector |  -  |
**502** | Bacen&#39;s SCR service is temporarily unavailable. Please try again later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

