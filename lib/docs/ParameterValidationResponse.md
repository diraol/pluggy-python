# ParameterValidationResponse

Response to parameter's validations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ParameterValidationError]**](ParameterValidationError.md) |  | [optional] 
**parameters** | **Dict[str, str]** | Key-Value credentials neccesary to create an item | [optional] 

## Example

```python
from pluggy_sdk.models.parameter_validation_response import ParameterValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterValidationResponse from a JSON string
parameter_validation_response_instance = ParameterValidationResponse.from_json(json)
# print the JSON string representation of the object
print(ParameterValidationResponse.to_json())

# convert the object into a dict
parameter_validation_response_dict = parameter_validation_response_instance.to_dict()
# create an instance of ParameterValidationResponse from a dict
parameter_validation_response_from_dict = ParameterValidationResponse.from_dict(parameter_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


