# CreateBoletoBoletoFine

Fine information for late payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Fine value | 
**type** | **str** | Type of fine calculation | 

## Example

```python
from pluggy_sdk.models.create_boleto_boleto_fine import CreateBoletoBoletoFine

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBoletoBoletoFine from a JSON string
create_boleto_boleto_fine_instance = CreateBoletoBoletoFine.from_json(json)
# print the JSON string representation of the object
print(CreateBoletoBoletoFine.to_json())

# convert the object into a dict
create_boleto_boleto_fine_dict = create_boleto_boleto_fine_instance.to_dict()
# create an instance of CreateBoletoBoletoFine from a dict
create_boleto_boleto_fine_from_dict = CreateBoletoBoletoFine.from_dict(create_boleto_boleto_fine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


