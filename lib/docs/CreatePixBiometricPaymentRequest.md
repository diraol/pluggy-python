# CreatePixBiometricPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount in BRL, with up to two decimal places. | 
**recipient_id** | **UUID** | Recipient that receives the payment. Bank account recipients only: smart accounts are not supported. | 
**description** | **str** | Shown to the payer. | [optional] 
**customer_id** | **UUID** | Payment Customer that identifies the payer. The payment page uses its CPF/CNPJ and does not ask for it; without it the payer types their CPF. | [optional] 
**client_payment_id** | **str** | Your own identifier for the payment. | [optional] 
**callback_urls** | [**PaymentRequestCallbackUrls**](PaymentRequestCallbackUrls.md) |  | [optional] 
**linked_journey** | **bool** | Offer the payer to also share their account balance and overdraft limit while the link lasts (optional for the payer). Read it with the enrollment balance endpoint. | [optional] [default to False]
**is_sandbox** | **bool** | Pix por biometria has no sandbox: &#x60;true&#x60; is rejected with &#x60;PIX_BIOMETRIC_SANDBOX_NOT_SUPPORTED&#x60;. | [optional] 

## Example

```python
from pluggy_sdk.models.create_pix_biometric_payment_request import CreatePixBiometricPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePixBiometricPaymentRequest from a JSON string
create_pix_biometric_payment_request_instance = CreatePixBiometricPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePixBiometricPaymentRequest.to_json())

# convert the object into a dict
create_pix_biometric_payment_request_dict = create_pix_biometric_payment_request_instance.to_dict()
# create an instance of CreatePixBiometricPaymentRequest from a dict
create_pix_biometric_payment_request_from_dict = CreatePixBiometricPaymentRequest.from_dict(create_pix_biometric_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


