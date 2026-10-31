# PaymentRequestPixBiometric

Present on Pix por biometria payment requests; null on every other kind.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_journey** | **bool** | Whether the payer was offered balance sharing. | 
**enrollment** | [**PixBiometricEnrollmentSummary**](PixBiometricEnrollmentSummary.md) | The linked account the request was paid with, with its current status. Null until the request is paid. | 

## Example

```python
from pluggy_sdk.models.payment_request_pix_biometric import PaymentRequestPixBiometric

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestPixBiometric from a JSON string
payment_request_pix_biometric_instance = PaymentRequestPixBiometric.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestPixBiometric.to_json())

# convert the object into a dict
payment_request_pix_biometric_dict = payment_request_pix_biometric_instance.to_dict()
# create an instance of PaymentRequestPixBiometric from a dict
payment_request_pix_biometric_from_dict = PaymentRequestPixBiometric.from_dict(payment_request_pix_biometric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


