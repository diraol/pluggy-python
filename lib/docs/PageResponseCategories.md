# PageResponseCategories

Paginated list of transaction categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Category]**](Category.md) | Categories for the current page | 
**page** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from pluggy_sdk.models.page_response_categories import PageResponseCategories

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseCategories from a JSON string
page_response_categories_instance = PageResponseCategories.from_json(json)
# print the JSON string representation of the object
print(PageResponseCategories.to_json())

# convert the object into a dict
page_response_categories_dict = page_response_categories_instance.to_dict()
# create an instance of PageResponseCategories from a dict
page_response_categories_from_dict = PageResponseCategories.from_dict(page_response_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


