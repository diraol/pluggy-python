# InvestmentTransaction

Movement of the investment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of transactions | 
**movement_type** | **str** | Type of movement of the transaction | [optional] 
**quantity** | **float** | Quantity of the transaction | [optional] 
**value** | **float** | Value on the transaction&#39;s Date | [optional] 
**amount** | **float** | Gross amount of the operation. May be null only if type is TRANSFER | [optional] 
**agreed_rate** | **float** | Agreed rate for treasury applications | [optional] 
**var_date** | **datetime** | Date when the transaction was made | 
**trade_date** | **datetime** | Date when the transaction was confirmed | [optional] 
**expenses** | [**InvestmentExpenses**](InvestmentExpenses.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.investment_transaction import InvestmentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentTransaction from a JSON string
investment_transaction_instance = InvestmentTransaction.from_json(json)
# print the JSON string representation of the object
print(InvestmentTransaction.to_json())

# convert the object into a dict
investment_transaction_dict = investment_transaction_instance.to_dict()
# create an instance of InvestmentTransaction from a dict
investment_transaction_from_dict = InvestmentTransaction.from_dict(investment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


