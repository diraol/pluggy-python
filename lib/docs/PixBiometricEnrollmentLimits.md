# PixBiometricEnrollmentLimits

Limits the payer set at the bank, in BRL. Null until the institution reports them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **float** | Per-payment limit | 
**daily** | **float** | Daily limit | 
**daily_used** | **float** | How much of today&#39;s limit is used | 

## Example

```python
from pluggy_sdk.models.pix_biometric_enrollment_limits import PixBiometricEnrollmentLimits

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricEnrollmentLimits from a JSON string
pix_biometric_enrollment_limits_instance = PixBiometricEnrollmentLimits.from_json(json)
# print the JSON string representation of the object
print(PixBiometricEnrollmentLimits.to_json())

# convert the object into a dict
pix_biometric_enrollment_limits_dict = pix_biometric_enrollment_limits_instance.to_dict()
# create an instance of PixBiometricEnrollmentLimits from a dict
pix_biometric_enrollment_limits_from_dict = PixBiometricEnrollmentLimits.from_dict(pix_biometric_enrollment_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


