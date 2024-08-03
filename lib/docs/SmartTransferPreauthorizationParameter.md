# SmartTransferPreauthorizationParameter

Credentials neccesary to create a smart transfer preauthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpf** | **str** | CPF of the payer | 
**cnpj** | **str** | CNPJ of the payer | [optional] 

## Example

```python
from pluggy_sdk.models.smart_transfer_preauthorization_parameter import SmartTransferPreauthorizationParameter

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPreauthorizationParameter from a JSON string
smart_transfer_preauthorization_parameter_instance = SmartTransferPreauthorizationParameter.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPreauthorizationParameter.to_json())

# convert the object into a dict
smart_transfer_preauthorization_parameter_dict = smart_transfer_preauthorization_parameter_instance.to_dict()
# create an instance of SmartTransferPreauthorizationParameter from a dict
smart_transfer_preauthorization_parameter_from_dict = SmartTransferPreauthorizationParameter.from_dict(smart_transfer_preauthorization_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


