# InvestmentExpenses

Taxes and fees that applied to the transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_tax** | **float** | (ISS) Service tax that varies according to state | [optional] 
**brokerage_fee** | **float** | Commission charged by the brokerage for carrying out transactions on the stock market | [optional] 
**income_tax** | **float** | (IRRF) Income Tax Withholding, amount paid to the Internal Revenue Service | [optional] 
**trading_assets_notice_fee** | **float** | (ANA) Fee of Notice of Trading in Assets | [optional] 
**maintenance_fee** | **float** | (termo/opções) Fees charged by BM&amp;F Bovespa in negotiations | [optional] 
**settlement_fee** | **float** | Liquidation fee for the settlement of a position on the expiration date or the financial settlement of physical delivery | [optional] 
**clearing_fee** | **float** | Registration fee | [optional] 
**stock_exchange_fee** | **float** | (Emolumentos) Fees charged by BM&amp;F Bovespa as a source of operating income | [optional] 
**custody_fee** | **float** | Fee by brokers to keep recordsin their home broker systems or on the trading desk | [optional] 
**operating_fee** | **float** | Amount paid to the Operator for the intermediation service | [optional] 
**other** | **float** | Sum of other not defined expenses | [optional] 

## Example

```python
from pluggy_sdk.models.investment_expenses import InvestmentExpenses

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentExpenses from a JSON string
investment_expenses_instance = InvestmentExpenses.from_json(json)
# print the JSON string representation of the object
print(InvestmentExpenses.to_json())

# convert the object into a dict
investment_expenses_dict = investment_expenses_instance.to_dict()
# create an instance of InvestmentExpenses from a dict
investment_expenses_from_dict = InvestmentExpenses.from_dict(investment_expenses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


