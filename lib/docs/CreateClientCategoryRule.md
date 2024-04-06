# CreateClientCategoryRule

Create client category rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the transaction rule. | 
**category_id** | **str** | Identifier of the category | 
**client_id** | **str** | Identifier of the client | 

## Example

```python
from pluggy_sdk.models.create_client_category_rule import CreateClientCategoryRule

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientCategoryRule from a JSON string
create_client_category_rule_instance = CreateClientCategoryRule.from_json(json)
# print the JSON string representation of the object
print(CreateClientCategoryRule.to_json())

# convert the object into a dict
create_client_category_rule_dict = create_client_category_rule_instance.to_dict()
# create an instance of CreateClientCategoryRule from a dict
create_client_category_rule_form_dict = create_client_category_rule.from_dict(create_client_category_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


