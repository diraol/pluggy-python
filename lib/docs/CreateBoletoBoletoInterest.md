# CreateBoletoBoletoInterest

Interest information for late payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Interest value | 
**type** | **str** | Type of interest calculation | 

## Example

```python
from pluggy_sdk.models.create_boleto_boleto_interest import CreateBoletoBoletoInterest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBoletoBoletoInterest from a JSON string
create_boleto_boleto_interest_instance = CreateBoletoBoletoInterest.from_json(json)
# print the JSON string representation of the object
print(CreateBoletoBoletoInterest.to_json())

# convert the object into a dict
create_boleto_boleto_interest_dict = create_boleto_boleto_interest_instance.to_dict()
# create an instance of CreateBoletoBoletoInterest from a dict
create_boleto_boleto_interest_from_dict = CreateBoletoBoletoInterest.from_dict(create_boleto_boleto_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


