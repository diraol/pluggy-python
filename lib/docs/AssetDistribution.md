# AssetDistribution

Structure of all assets that comprises the asset-portfolio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investment_type** | **float** | investment type within user assets-portfolio and amount of type of asset that comprises the aggregated asstets-portfolio | [optional] 

## Example

```python
from openapi_client.models.asset_distribution import AssetDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDistribution from a JSON string
asset_distribution_instance = AssetDistribution.from_json(json)
# print the JSON string representation of the object
print(AssetDistribution.to_json())

# convert the object into a dict
asset_distribution_dict = asset_distribution_instance.to_dict()
# create an instance of AssetDistribution from a dict
asset_distribution_form_dict = asset_distribution.from_dict(asset_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


