# Category

Cateogry response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the category | 
**description** | **str** | Description of the category | 
**description_translated** | **str** | Description of the category, translated to portuguese | [optional] 
**parent_id** | **str** | Parent&#39;s identifier | [optional] 
**parent_description** | **str** | Parent&#39;s category description | [optional] 

## Example

```python
from pluggy_sdk.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_form_dict = category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


