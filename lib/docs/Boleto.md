# Boleto

Boleto data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digitable_line** | **str** | Boleto digitable line | 
**barcode** | **str** | Boleto barcode | 
**payer** | [**BoletoPayer**](BoletoPayer.md) |  | 
**recipient** | [**BoletoRecipient**](BoletoRecipient.md) |  | 
**var_date** | **datetime** | Boleto issue date | 
**due_date** | **datetime** | Boleto due date | [optional] 
**expiration_date** | **datetime** | After this date, the boleto cannot be paid | 
**base_amount** | **float** | Boleto original amount, without interests, penalties and discounts | 
**penalty_amount** | **float** | Boleto penalty amount. If there is no penalty, it will be returned as zero | 
**interest_amount** | **float** | Boleto interest amount. If there is no interest, it will be returned as zero | [optional] 
**discount_amount** | **float** | Boleto discount amount. If there is no discounts, it will be returned as zero | 
**total_amount** | **float** | Boleto final amount. It is equal to the base amount plus penalties and interests, minus discounts | 
**updated_at** | **datetime** | Date when the lastest information of this boleto has been retrieved | [optional] 

## Example

```python
from pluggy_sdk.models.boleto import Boleto

# TODO update the JSON string below
json = "{}"
# create an instance of Boleto from a JSON string
boleto_instance = Boleto.from_json(json)
# print the JSON string representation of the object
print(Boleto.to_json())

# convert the object into a dict
boleto_dict = boleto_instance.to_dict()
# create an instance of Boleto from a dict
boleto_from_dict = Boleto.from_dict(boleto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


