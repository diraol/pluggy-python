# AggregatedPortfolioResponse

Response with overview of the distribution and yield of all the assets the user has in a period of time indicated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[AggregatedPortfolio]**](AggregatedPortfolio.md) | Snapshot of assets-portfolio by period indicated | [optional] 

## Example

```python
from openapi_client.models.aggregated_portfolio_response import AggregatedPortfolioResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedPortfolioResponse from a JSON string
aggregated_portfolio_response_instance = AggregatedPortfolioResponse.from_json(json)
# print the JSON string representation of the object
print(AggregatedPortfolioResponse.to_json())

# convert the object into a dict
aggregated_portfolio_response_dict = aggregated_portfolio_response_instance.to_dict()
# create an instance of AggregatedPortfolioResponse from a dict
aggregated_portfolio_response_form_dict = aggregated_portfolio_response.from_dict(aggregated_portfolio_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


