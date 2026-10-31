# PixBiometricEnrollmentsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[PixBiometricEnrollment]**](PixBiometricEnrollment.md) | List of enrollments | [optional] 

## Example

```python
from pluggy_sdk.models.pix_biometric_enrollments_list200_response import PixBiometricEnrollmentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricEnrollmentsList200Response from a JSON string
pix_biometric_enrollments_list200_response_instance = PixBiometricEnrollmentsList200Response.from_json(json)
# print the JSON string representation of the object
print(PixBiometricEnrollmentsList200Response.to_json())

# convert the object into a dict
pix_biometric_enrollments_list200_response_dict = pix_biometric_enrollments_list200_response_instance.to_dict()
# create an instance of PixBiometricEnrollmentsList200Response from a dict
pix_biometric_enrollments_list200_response_from_dict = PixBiometricEnrollmentsList200Response.from_dict(pix_biometric_enrollments_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


