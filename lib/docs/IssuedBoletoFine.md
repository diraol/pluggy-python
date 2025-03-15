# IssuedBoletoFine

Fine information for late payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Fine value | [optional] 
**type** | **str** | Type of fine calculation | [optional] 

## Example

```python
from pluggy_sdk.models.issued_boleto_fine import IssuedBoletoFine

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedBoletoFine from a JSON string
issued_boleto_fine_instance = IssuedBoletoFine.from_json(json)
# print the JSON string representation of the object
print(IssuedBoletoFine.to_json())

# convert the object into a dict
issued_boleto_fine_dict = issued_boleto_fine_instance.to_dict()
# create an instance of IssuedBoletoFine from a dict
issued_boleto_fine_from_dict = IssuedBoletoFine.from_dict(issued_boleto_fine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


