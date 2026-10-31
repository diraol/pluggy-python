# PixBiometricEnrollmentConnector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Connector primary identifier | 
**name** | **str** | Institution name | 
**image_url** | **str** | Institution logo | 

## Example

```python
from pluggy_sdk.models.pix_biometric_enrollment_connector import PixBiometricEnrollmentConnector

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricEnrollmentConnector from a JSON string
pix_biometric_enrollment_connector_instance = PixBiometricEnrollmentConnector.from_json(json)
# print the JSON string representation of the object
print(PixBiometricEnrollmentConnector.to_json())

# convert the object into a dict
pix_biometric_enrollment_connector_dict = pix_biometric_enrollment_connector_instance.to_dict()
# create an instance of PixBiometricEnrollmentConnector from a dict
pix_biometric_enrollment_connector_from_dict = PixBiometricEnrollmentConnector.from_dict(pix_biometric_enrollment_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


