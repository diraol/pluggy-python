# MonthlyPortfolio

Response with overview of the distribution and yield of all the assets the user has month by month

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Current balance from total portfolio of assets | [optional] 
**yield_percentage** | **float** | Percentage yield compared to the previous month | [optional] 
**yield_amount** | **float** | Amount yield over the period | [optional] 
**var_date** | **str** | First day of the month retrieved | [optional] 
**yield_percentage_over_index** | [**PercentageOverIndex**](PercentageOverIndex.md) |  | [optional] 

## Example

```python
from openapi_client.models.monthly_portfolio import MonthlyPortfolio

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyPortfolio from a JSON string
monthly_portfolio_instance = MonthlyPortfolio.from_json(json)
# print the JSON string representation of the object
print(MonthlyPortfolio.to_json())

# convert the object into a dict
monthly_portfolio_dict = monthly_portfolio_instance.to_dict()
# create an instance of MonthlyPortfolio from a dict
monthly_portfolio_form_dict = monthly_portfolio.from_dict(monthly_portfolio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


