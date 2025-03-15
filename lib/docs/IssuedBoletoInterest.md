# IssuedBoletoInterest

Interest information for late payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Interest value | [optional] 
**type** | **str** | Type of interest calculation | [optional] 

## Example

```python
from pluggy_sdk.models.issued_boleto_interest import IssuedBoletoInterest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedBoletoInterest from a JSON string
issued_boleto_interest_instance = IssuedBoletoInterest.from_json(json)
# print the JSON string representation of the object
print(IssuedBoletoInterest.to_json())

# convert the object into a dict
issued_boleto_interest_dict = issued_boleto_interest_instance.to_dict()
# create an instance of IssuedBoletoInterest from a dict
issued_boleto_interest_from_dict = IssuedBoletoInterest.from_dict(issued_boleto_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


