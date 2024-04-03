# PercentageOverIndex

Indicates the value bellow or over that the portfolio yield against the index indicated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | amount yield over or bellow indicated index | [optional] 
**index** | **str** | index used to reflect yield of portfolio | [optional] 

## Example

```python
from openapi_client.models.percentage_over_index import PercentageOverIndex

# TODO update the JSON string below
json = "{}"
# create an instance of PercentageOverIndex from a JSON string
percentage_over_index_instance = PercentageOverIndex.from_json(json)
# print the JSON string representation of the object
print(PercentageOverIndex.to_json())

# convert the object into a dict
percentage_over_index_dict = percentage_over_index_instance.to_dict()
# create an instance of PercentageOverIndex from a dict
percentage_over_index_form_dict = percentage_over_index.from_dict(percentage_over_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


