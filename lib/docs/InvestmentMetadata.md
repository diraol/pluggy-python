# InvestmentMetadata

Investment metadata for Previdencia migrations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_regime** | **str** | Description of the type of tax applied to previdencia | [optional] 
**proposal_number** | **str** | Previdencial proposal number | [optional] 
**process_number** | **str** | Number of the process of a previdencia | [optional] 
**fund_name** | **str** | Name of the fund associated with the previdencia. | [optional] 
**insurer** | [**Company**](.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.investment_metadata import InvestmentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentMetadata from a JSON string
investment_metadata_instance = InvestmentMetadata.from_json(json)
# print the JSON string representation of the object
print(InvestmentMetadata.to_json())

# convert the object into a dict
investment_metadata_dict = investment_metadata_instance.to_dict()
# create an instance of InvestmentMetadata from a dict
investment_metadata_from_dict = InvestmentMetadata.from_dict(investment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


