# IssuedBoletoPayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** | Payer tax number (CPF/CNPJ) | 
**person_type** | **str** | Type of person (individual or business) | [optional] 
**name** | **str** | Payer name | 
**address_street** | **str** | Payer street address | [optional] 
**address_number** | **str** | Payer address number | [optional] 
**address_complement** | **str** | Additional address information | [optional] 
**address_neighborhood** | **str** | Payer neighborhood | [optional] 
**address_city** | **str** | Payer city | [optional] 
**address_state** | **str** | Payer state | 
**address_zip_code** | **str** | Payer ZIP code | 
**email** | **str** | Payer email | [optional] 
**ddd** | **str** | Payer area code | [optional] 
**phone_number** | **str** | Payer phone number | [optional] 
**amount_paid** | **float** | Amount paid or null if it hasn&#39;t been paid yet | [optional] 
**payment_origin** | **str** | Payment origin for the boleto | [optional] 

## Example

```python
from pluggy_sdk.models.issued_boleto_payer import IssuedBoletoPayer

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedBoletoPayer from a JSON string
issued_boleto_payer_instance = IssuedBoletoPayer.from_json(json)
# print the JSON string representation of the object
print(IssuedBoletoPayer.to_json())

# convert the object into a dict
issued_boleto_payer_dict = issued_boleto_payer_instance.to_dict()
# create an instance of IssuedBoletoPayer from a dict
issued_boleto_payer_from_dict = IssuedBoletoPayer.from_dict(issued_boleto_payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


