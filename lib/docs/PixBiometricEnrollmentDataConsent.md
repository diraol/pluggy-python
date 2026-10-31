# PixBiometricEnrollmentDataConsent

Balance-sharing permission. Null when the payment request did not offer it or the payer chose not to share.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | AUTHORISED: the balance can be read. | 
**rejection_reason** | **str** | Why it was rejected | 
**updated_at** | **datetime** | When Pluggy last saw the status change | 

## Example

```python
from pluggy_sdk.models.pix_biometric_enrollment_data_consent import PixBiometricEnrollmentDataConsent

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricEnrollmentDataConsent from a JSON string
pix_biometric_enrollment_data_consent_instance = PixBiometricEnrollmentDataConsent.from_json(json)
# print the JSON string representation of the object
print(PixBiometricEnrollmentDataConsent.to_json())

# convert the object into a dict
pix_biometric_enrollment_data_consent_dict = pix_biometric_enrollment_data_consent_instance.to_dict()
# create an instance of PixBiometricEnrollmentDataConsent from a dict
pix_biometric_enrollment_data_consent_from_dict = PixBiometricEnrollmentDataConsent.from_dict(pix_biometric_enrollment_data_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


