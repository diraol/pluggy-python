# PageResponseCategoryRules



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClientCategoryRule]**](ClientCategoryRule.md) |  | 
**page** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from openapi_client.models.page_response_category_rules import PageResponseCategoryRules

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseCategoryRules from a JSON string
page_response_category_rules_instance = PageResponseCategoryRules.from_json(json)
# print the JSON string representation of the object
print(PageResponseCategoryRules.to_json())

# convert the object into a dict
page_response_category_rules_dict = page_response_category_rules_instance.to_dict()
# create an instance of PageResponseCategoryRules from a dict
page_response_category_rules_form_dict = page_response_category_rules.from_dict(page_response_category_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


