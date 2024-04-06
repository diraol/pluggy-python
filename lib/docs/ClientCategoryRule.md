# ClientCategoryRule

Category rule by client id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the transaction rule. | 
**category_id** | **str** | Identifier of the category | [optional] 
**category** | **str** | Description of the category | 
**client_id** | **str** | Identifier of the client | [optional] 

## Example

```python
from pluggy_sdk.models.client_category_rule import ClientCategoryRule

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCategoryRule from a JSON string
client_category_rule_instance = ClientCategoryRule.from_json(json)
# print the JSON string representation of the object
print(ClientCategoryRule.to_json())

# convert the object into a dict
client_category_rule_dict = client_category_rule_instance.to_dict()
# create an instance of ClientCategoryRule from a dict
client_category_rule_form_dict = client_category_rule.from_dict(client_category_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


