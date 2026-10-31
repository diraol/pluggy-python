# PixBiometricEnrollmentSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Enrollment primary identifier | 
**status** | **str** | CREATED: the payer started linking and has not finished. AUTHORIZED: the link is active. REJECTED: the link was not completed (rejected, or not finished in time). REVOKED: revoked at the bank or through the API. EXPIRED: the link reached its expiration date or became inactive at the institution. REJECTED, REVOKED and EXPIRED are final. | 
**connector** | [**PixBiometricEnrollmentConnector**](PixBiometricEnrollmentConnector.md) | Institution where the account is held | 
**debtor** | [**PixBiometricDebtor**](PixBiometricDebtor.md) | The linked account. Null until the institution reports it. | 

## Example

```python
from pluggy_sdk.models.pix_biometric_enrollment_summary import PixBiometricEnrollmentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricEnrollmentSummary from a JSON string
pix_biometric_enrollment_summary_instance = PixBiometricEnrollmentSummary.from_json(json)
# print the JSON string representation of the object
print(PixBiometricEnrollmentSummary.to_json())

# convert the object into a dict
pix_biometric_enrollment_summary_dict = pix_biometric_enrollment_summary_instance.to_dict()
# create an instance of PixBiometricEnrollmentSummary from a dict
pix_biometric_enrollment_summary_from_dict = PixBiometricEnrollmentSummary.from_dict(pix_biometric_enrollment_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


