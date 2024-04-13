# MonthlyPortfolioResponse

Response with overview of the distribution and yield of all the assets the user has month by month

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[MonthlyPortfolio]**](MonthlyPortfolio.md) | Array with overview of the distribution and yield of all the assets the user has month by month | [optional] 

## Example

```python
from pluggy_sdk.models.monthly_portfolio_response import MonthlyPortfolioResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyPortfolioResponse from a JSON string
monthly_portfolio_response_instance = MonthlyPortfolioResponse.from_json(json)
# print the JSON string representation of the object
print(MonthlyPortfolioResponse.to_json())

# convert the object into a dict
monthly_portfolio_response_dict = monthly_portfolio_response_instance.to_dict()
# create an instance of MonthlyPortfolioResponse from a dict
monthly_portfolio_response_from_dict = MonthlyPortfolioResponse.from_dict(monthly_portfolio_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


