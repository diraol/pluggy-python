# InvestmentTransaction

Movement of the investment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary investment transaction identifier | 
**type** | **str** | Operation performed on the investment position. - &#x60;BUY&#x60;: subscription / purchase of new quotas. - &#x60;SELL&#x60;: redemption / sale of quotas. - &#x60;TRANSFER&#x60;: portability or internal transfer between accounts (the &#x60;amount&#x60; field may be null). - &#x60;TAX&#x60;: tax withholdings such as IR or IOF. - &#x60;INTEREST&#x60;: interest or yield credited to the position. - &#x60;AMORTIZATION&#x60;: principal repayment (typical of fixed-income amortizing bonds). | 
**movement_type** | **str** | Cash-flow direction of the transaction from the holder&#39;s perspective. - &#x60;CREDIT&#x60;: money goes into the position (defaults for &#x60;BUY&#x60;). - &#x60;DEBIT&#x60;: money leaves the position (defaults for &#x60;SELL&#x60;, &#x60;TAX&#x60;, &#x60;TRANSFER&#x60;, &#x60;INTEREST&#x60;, &#x60;AMORTIZATION&#x60;). | [optional] 
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


