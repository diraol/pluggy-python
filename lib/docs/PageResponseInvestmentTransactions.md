# PageResponseInvestmentTransactions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[InvestmentTransaction]**](InvestmentTransaction.md) |  | 
**page** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from pluggy_sdk.models.page_response_investment_transactions import PageResponseInvestmentTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseInvestmentTransactions from a JSON string
page_response_investment_transactions_instance = PageResponseInvestmentTransactions.from_json(json)
# print the JSON string representation of the object
print(PageResponseInvestmentTransactions.to_json())

# convert the object into a dict
page_response_investment_transactions_dict = page_response_investment_transactions_instance.to_dict()
# create an instance of PageResponseInvestmentTransactions from a dict
page_response_investment_transactions_from_dict = PageResponseInvestmentTransactions.from_dict(page_response_investment_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


