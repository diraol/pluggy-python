# AggregatedPortfolio

Array of Aggregated Portfolio by period indicated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Current balance from total portfolio of assets | [optional] 
**percentage** | **float** | Percentage yield compared to the previous month | [optional] 
**amount** | **float** | Amount yield over the period | [optional] 
**currency** | **str** | Currency of the yield amount | [optional] 
**var_date** | **str** | Date when the porfolio was captured | [optional] 
**percentage_over_index** | [**PercentageOverIndex**](PercentageOverIndex.md) |  | [optional] 
**period** | **str** | Period from AggregatedPortfolio was retrieved | [optional] 
**asset_distribution** | [**AssetDistribution**](AssetDistribution.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.aggregated_portfolio import AggregatedPortfolio

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedPortfolio from a JSON string
aggregated_portfolio_instance = AggregatedPortfolio.from_json(json)
# print the JSON string representation of the object
print(AggregatedPortfolio.to_json())

# convert the object into a dict
aggregated_portfolio_dict = aggregated_portfolio_instance.to_dict()
# create an instance of AggregatedPortfolio from a dict
aggregated_portfolio_form_dict = aggregated_portfolio.from_dict(aggregated_portfolio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


