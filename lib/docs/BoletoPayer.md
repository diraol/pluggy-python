# BoletoPayer

Boleto payer information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** | Payer CPF or CNPJ | 
**name** | **str** | Payer name | 

## Example

```python
from pluggy_sdk.models.boleto_payer import BoletoPayer

# TODO update the JSON string below
json = "{}"
# create an instance of BoletoPayer from a JSON string
boleto_payer_instance = BoletoPayer.from_json(json)
# print the JSON string representation of the object
print(BoletoPayer.to_json())

# convert the object into a dict
boleto_payer_dict = boleto_payer_instance.to_dict()
# create an instance of BoletoPayer from a dict
boleto_payer_from_dict = BoletoPayer.from_dict(boleto_payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


