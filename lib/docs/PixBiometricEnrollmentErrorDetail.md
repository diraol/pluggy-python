# PixBiometricEnrollmentErrorDetail

Reason the institution gave when the link was rejected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from pluggy_sdk.models.pix_biometric_enrollment_error_detail import PixBiometricEnrollmentErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricEnrollmentErrorDetail from a JSON string
pix_biometric_enrollment_error_detail_instance = PixBiometricEnrollmentErrorDetail.from_json(json)
# print the JSON string representation of the object
print(PixBiometricEnrollmentErrorDetail.to_json())

# convert the object into a dict
pix_biometric_enrollment_error_detail_dict = pix_biometric_enrollment_error_detail_instance.to_dict()
# create an instance of PixBiometricEnrollmentErrorDetail from a dict
pix_biometric_enrollment_error_detail_from_dict = PixBiometricEnrollmentErrorDetail.from_dict(pix_biometric_enrollment_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


