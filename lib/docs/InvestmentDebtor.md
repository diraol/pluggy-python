# InvestmentDebtor

Underlying debtor of receivables-backed paper (CRI / CRA)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the underlying debtor | [optional] 

## Example

```python
from pluggy_sdk.models.investment_debtor import InvestmentDebtor

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentDebtor from a JSON string
investment_debtor_instance = InvestmentDebtor.from_json(json)
# print the JSON string representation of the object
print(InvestmentDebtor.to_json())

# convert the object into a dict
investment_debtor_dict = investment_debtor_instance.to_dict()
# create an instance of InvestmentDebtor from a dict
investment_debtor_from_dict = InvestmentDebtor.from_dict(investment_debtor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


