# CreateBoletoBoletoPayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** | Payer tax number (CPF/CNPJ) | 
**name** | **str** | Payer name | 
**address_street** | **str** | Payer street address | [optional] 
**address_city** | **str** | Payer city | [optional] 
**address_state** | **str** | Payer state | 
**address_zip_code** | **str** | Payer ZIP code | 

## Example

```python
from pluggy_sdk.models.create_boleto_boleto_payer import CreateBoletoBoletoPayer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBoletoBoletoPayer from a JSON string
create_boleto_boleto_payer_instance = CreateBoletoBoletoPayer.from_json(json)
# print the JSON string representation of the object
print(CreateBoletoBoletoPayer.to_json())

# convert the object into a dict
create_boleto_boleto_payer_dict = create_boleto_boleto_payer_instance.to_dict()
# create an instance of CreateBoletoBoletoPayer from a dict
create_boleto_boleto_payer_from_dict = CreateBoletoBoletoPayer.from_dict(create_boleto_boleto_payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


