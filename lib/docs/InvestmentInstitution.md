# InvestmentInstitution

Financial institution holding the investment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full name of the institution | 
**number** | **str** | Identifier of the institution (CNPJ or other) | 

## Example

```python
from pluggy_sdk.models.investment_institution import InvestmentInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentInstitution from a JSON string
investment_institution_instance = InvestmentInstitution.from_json(json)
# print the JSON string representation of the object
print(InvestmentInstitution.to_json())

# convert the object into a dict
investment_institution_dict = investment_institution_instance.to_dict()
# create an instance of InvestmentInstitution from a dict
investment_institution_from_dict = InvestmentInstitution.from_dict(investment_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


