# CreateBoletoBoleto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seu_numero** | **str** | Your identifier for this boleto | 
**amount** | **float** | Boleto amount | 
**due_date** | **datetime** | Due date for the boleto. Must be today or in the future. | 
**payer** | [**CreateBoletoBoletoPayer**](CreateBoletoBoletoPayer.md) |  | 
**fine** | [**CreateBoletoBoletoFine**](CreateBoletoBoletoFine.md) |  | [optional] 
**interest** | [**CreateBoletoBoletoInterest**](CreateBoletoBoletoInterest.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.create_boleto_boleto import CreateBoletoBoleto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBoletoBoleto from a JSON string
create_boleto_boleto_instance = CreateBoletoBoleto.from_json(json)
# print the JSON string representation of the object
print(CreateBoletoBoleto.to_json())

# convert the object into a dict
create_boleto_boleto_dict = create_boleto_boleto_instance.to_dict()
# create an instance of CreateBoletoBoleto from a dict
create_boleto_boleto_from_dict = CreateBoletoBoleto.from_dict(create_boleto_boleto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


