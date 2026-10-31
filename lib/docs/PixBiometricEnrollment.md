# PixBiometricEnrollment

A linked account (enrollment): the payer's account at one institution, linked to the device and browser where they created the passkey. Only the payer creates one, on the payment page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Enrollment primary identifier. Payment intents reference it as &#x60;enrollmentId&#x60;. | 
**status** | **str** | CREATED: the payer started linking and has not finished. AUTHORIZED: the link is active. REJECTED: the link was not completed (rejected, or not finished in time). REVOKED: revoked at the bank or through the API. EXPIRED: the link reached its expiration date or became inactive at the institution. REJECTED, REVOKED and EXPIRED are final. | 
**connector** | [**PixBiometricEnrollmentConnector**](PixBiometricEnrollmentConnector.md) | Institution where the account is held | 
**debtor** | [**PixBiometricDebtor**](PixBiometricDebtor.md) | The linked account. Null until the institution reports it. | 
**cpf** | **str** | Payer&#39;s CPF, masked | 
**cnpj** | **str** | Payer&#39;s CNPJ, masked | 
**customer_id** | **UUID** | Payment Customer of the payment request where the link was created. Null when the payer typed their CPF. | 
**limits** | [**PixBiometricEnrollmentLimits**](PixBiometricEnrollmentLimits.md) |  | 
**expires_at** | **datetime** | When the link expires, as set by the institution | 
**data_consent** | [**PixBiometricEnrollmentDataConsent**](PixBiometricEnrollmentDataConsent.md) |  | 
**revoked_by** | **str** | Who revoked the link: BANK (the payer or the institution, at the bank) or CLIENT (you, through the API). Null unless &#x60;status&#x60; is REVOKED. | 
**error_detail** | [**PixBiometricEnrollmentErrorDetail**](PixBiometricEnrollmentErrorDetail.md) |  | 
**created_at** | **datetime** | Date the enrollment was created | 
**updated_at** | **datetime** | Date the enrollment was last updated | 

## Example

```python
from pluggy_sdk.models.pix_biometric_enrollment import PixBiometricEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricEnrollment from a JSON string
pix_biometric_enrollment_instance = PixBiometricEnrollment.from_json(json)
# print the JSON string representation of the object
print(PixBiometricEnrollment.to_json())

# convert the object into a dict
pix_biometric_enrollment_dict = pix_biometric_enrollment_instance.to_dict()
# create an instance of PixBiometricEnrollment from a dict
pix_biometric_enrollment_from_dict = PixBiometricEnrollment.from_dict(pix_biometric_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


