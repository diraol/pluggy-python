# ParameterValidationError



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**parameter** | **str** |  | 

## Example

```python
from pluggy_sdk.models.parameter_validation_error import ParameterValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterValidationError from a JSON string
parameter_validation_error_instance = ParameterValidationError.from_json(json)
# print the JSON string representation of the object
print(ParameterValidationError.to_json())

# convert the object into a dict
parameter_validation_error_dict = parameter_validation_error_instance.to_dict()
# create an instance of ParameterValidationError from a dict
parameter_validation_error_form_dict = parameter_validation_error.from_dict(parameter_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


