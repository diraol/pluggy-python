# pluggy_sdk.PixPorBiometriaApi

All URIs are relative to *https://api.pluggy.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_request_create_pix_biometric**](PixPorBiometriaApi.md#payment_request_create_pix_biometric) | **POST** /payments/requests/pix-biometric | Create Pix por biometria payment request
[**pix_biometric_enrollment_balance_retrieve**](PixPorBiometriaApi.md#pix_biometric_enrollment_balance_retrieve) | **GET** /pix-biometric/enrollments/{id}/balance | Retrieve account balance
[**pix_biometric_enrollment_data_consent_delete**](PixPorBiometriaApi.md#pix_biometric_enrollment_data_consent_delete) | **DELETE** /pix-biometric/enrollments/{id}/data-consent | Cancel balance permission
[**pix_biometric_enrollment_retrieve**](PixPorBiometriaApi.md#pix_biometric_enrollment_retrieve) | **GET** /pix-biometric/enrollments/{id} | Retrieve enrollment
[**pix_biometric_enrollment_revoke**](PixPorBiometriaApi.md#pix_biometric_enrollment_revoke) | **POST** /pix-biometric/enrollments/{id}/revoke | Revoke enrollment
[**pix_biometric_enrollments_list**](PixPorBiometriaApi.md#pix_biometric_enrollments_list) | **GET** /pix-biometric/enrollments | List enrollments


# **payment_request_create_pix_biometric**
> PaymentRequest payment_request_create_pix_biometric(create_pix_biometric_payment_request=create_pix_biometric_payment_request)

Create Pix por biometria payment request

Creates a payment request paid with Pix por biometria. Send its `paymentUrl` to the payer: on the first payment on a device they link an account at their bank and create a passkey; later payments on that device are confirmed with biometrics, without a bank redirect. One payment request per purchase. Not available in sandbox.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.create_pix_biometric_payment_request import CreatePixBiometricPaymentRequest
from pluggy_sdk.models.payment_request import PaymentRequest
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
    api_instance = pluggy_sdk.PixPorBiometriaApi(api_client)
    create_pix_biometric_payment_request = {"amount":149.9,"recipientId":"ab276a3d-17ba-47eb-97bf-688475037ffe","description":"Order 4821","customerId":"a2d4c1e8-5b7f-4c3a-9e2d-1f6b8c0d7e55","clientPaymentId":"4821","linkedJourney":false} # CreatePixBiometricPaymentRequest |  (optional)

    try:
        # Create Pix por biometria payment request
        api_response = api_instance.payment_request_create_pix_biometric(create_pix_biometric_payment_request=create_pix_biometric_payment_request)
        print("The response of PixPorBiometriaApi->payment_request_create_pix_biometric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PixPorBiometriaApi->payment_request_create_pix_biometric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pix_biometric_payment_request** | [**CreatePixBiometricPaymentRequest**](CreatePixBiometricPaymentRequest.md)|  | [optional] 

### Return type

[**PaymentRequest**](PaymentRequest.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payment request |  -  |
**400** | Invalid parameters, a sandbox request, or a smart account recipient |  -  |
**403** | Payment Initiation is not enabled for the client |  -  |
**404** | Recipient or customer not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pix_biometric_enrollment_balance_retrieve**
> PixBiometricBalance pix_biometric_enrollment_balance_retrieve(id)

Retrieve account balance

Reads the linked account balance in real time from the institution. Requires an AUTHORIZED enrollment created from a payment request with `linkedJourney`, whose `dataConsent` is `AUTHORISED`. Every call counts toward the institution's monthly Open Finance quota for that account; see [Operational Rate Limits](https://docs.pluggy.ai/docs/open-finance/rate-limits).

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.pix_biometric_balance import PixBiometricBalance
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
    api_instance = pluggy_sdk.PixPorBiometriaApi(api_client)
    id = UUID('c91a5e2b-7d0f-4f3e-9a51-2f6b8e1d4c77') # UUID | Enrollment primary identifier

    try:
        # Retrieve account balance
        api_response = api_instance.pix_biometric_enrollment_balance_retrieve(id)
        print("The response of PixPorBiometriaApi->pix_biometric_enrollment_balance_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PixPorBiometriaApi->pix_biometric_enrollment_balance_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Enrollment primary identifier | 

### Return type

[**PixBiometricBalance**](PixBiometricBalance.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account balance |  -  |
**403** | The enrollment is not AUTHORIZED, or the payer did not share the balance, or the permission ended |  -  |
**404** | Enrollment not found |  -  |
**429** | Rate limit reached. The account&#39;s monthly balance quota at the institution is the usual cause; try again later |  -  |
**502** | The institution could not be reached; try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pix_biometric_enrollment_data_consent_delete**
> PixBiometricEnrollment pix_biometric_enrollment_data_consent_delete(id)

Cancel balance permission

Cancels only the balance permission: the enrollment stays AUTHORIZED and payments keep working. Returns the enrollment with `dataConsent.status` REVOKED. A permission that already ended answers 200 unchanged, so retrying is safe.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.pix_biometric_enrollment import PixBiometricEnrollment
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
    api_instance = pluggy_sdk.PixPorBiometriaApi(api_client)
    id = UUID('c91a5e2b-7d0f-4f3e-9a51-2f6b8e1d4c77') # UUID | Enrollment primary identifier

    try:
        # Cancel balance permission
        api_response = api_instance.pix_biometric_enrollment_data_consent_delete(id)
        print("The response of PixPorBiometriaApi->pix_biometric_enrollment_data_consent_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PixPorBiometriaApi->pix_biometric_enrollment_data_consent_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Enrollment primary identifier | 

### Return type

[**PixBiometricEnrollment**](PixBiometricEnrollment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The enrollment, with the cancelled permission |  -  |
**403** | The enrollment has no balance permission |  -  |
**404** | Enrollment not found |  -  |
**502** | The institution could not be reached; try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pix_biometric_enrollment_retrieve**
> PixBiometricEnrollment pix_biometric_enrollment_retrieve(id)

Retrieve enrollment

Returns the enrollment, refreshed from the institution while it is not final, so a link revoked at the bank shows as REVOKED.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.pix_biometric_enrollment import PixBiometricEnrollment
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
    api_instance = pluggy_sdk.PixPorBiometriaApi(api_client)
    id = UUID('c91a5e2b-7d0f-4f3e-9a51-2f6b8e1d4c77') # UUID | Enrollment primary identifier

    try:
        # Retrieve enrollment
        api_response = api_instance.pix_biometric_enrollment_retrieve(id)
        print("The response of PixPorBiometriaApi->pix_biometric_enrollment_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PixPorBiometriaApi->pix_biometric_enrollment_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Enrollment primary identifier | 

### Return type

[**PixBiometricEnrollment**](PixBiometricEnrollment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The enrollment |  -  |
**404** | Enrollment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pix_biometric_enrollment_revoke**
> PixBiometricEnrollment pix_biometric_enrollment_revoke(id)

Revoke enrollment

Revokes the link at the institution. Returns the enrollment with status REVOKED and revokedBy CLIENT, and sends `pix_biometric_enrollment/revoked`. It cannot be undone: the payer links again to pay with biometrics. An enrollment already REJECTED, REVOKED or EXPIRED is returned unchanged, so retrying is safe.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.pix_biometric_enrollment import PixBiometricEnrollment
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
    api_instance = pluggy_sdk.PixPorBiometriaApi(api_client)
    id = UUID('c91a5e2b-7d0f-4f3e-9a51-2f6b8e1d4c77') # UUID | Enrollment primary identifier

    try:
        # Revoke enrollment
        api_response = api_instance.pix_biometric_enrollment_revoke(id)
        print("The response of PixPorBiometriaApi->pix_biometric_enrollment_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PixPorBiometriaApi->pix_biometric_enrollment_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Enrollment primary identifier | 

### Return type

[**PixBiometricEnrollment**](PixBiometricEnrollment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The revoked enrollment |  -  |
**404** | Enrollment not found |  -  |
**422** | The institution rejected the request |  -  |
**502** | The institution could not be reached; try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pix_biometric_enrollments_list**
> PixBiometricEnrollmentsList200Response pix_biometric_enrollments_list(customer_id=customer_id, cpf=cpf, cnpj=cnpj, status=status, page=page, page_size=page_size)

List enrollments

Lists the accounts your payers linked for Pix por biometria. A payer can have several: one per device and browser, and one per institution.

### Example

* Api Key Authentication (default):

```python
import pluggy_sdk
from pluggy_sdk.models.pix_biometric_enrollments_list200_response import PixBiometricEnrollmentsList200Response
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
    api_instance = pluggy_sdk.PixPorBiometriaApi(api_client)
    customer_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Enrollments created in payment requests for this Payment Customer (optional)
    cpf = 'cpf_example' # str | Payer's CPF, digits only (optional)
    cnpj = 'cnpj_example' # str | Payer's CNPJ, digits only (optional)
    status = 'status_example' # str | Enrollment status (optional)
    page = 56 # int | Page number (optional)
    page_size = 56 # int | Page size (optional)

    try:
        # List enrollments
        api_response = api_instance.pix_biometric_enrollments_list(customer_id=customer_id, cpf=cpf, cnpj=cnpj, status=status, page=page, page_size=page_size)
        print("The response of PixPorBiometriaApi->pix_biometric_enrollments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PixPorBiometriaApi->pix_biometric_enrollments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **UUID**| Enrollments created in payment requests for this Payment Customer | [optional] 
 **cpf** | **str**| Payer&#39;s CPF, digits only | [optional] 
 **cnpj** | **str**| Payer&#39;s CNPJ, digits only | [optional] 
 **status** | **str**| Enrollment status | [optional] 
 **page** | **int**| Page number | [optional] 
 **page_size** | **int**| Page size | [optional] 

### Return type

[**PixBiometricEnrollmentsList200Response**](PixBiometricEnrollmentsList200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The enrollments |  -  |
**403** | Payment Initiation is not enabled for the client |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

