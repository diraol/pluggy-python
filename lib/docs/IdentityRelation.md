# IdentityRelation

The relation object contains name and relation to the owner of the account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of relation: Father, Mother or Spouse | [optional] 
**name** | **str** | The full name of the person | [optional] 
**document** | **str** | Primary document of the person | [optional] 

## Example

```python
from pluggy_sdk.models.identity_relation import IdentityRelation

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityRelation from a JSON string
identity_relation_instance = IdentityRelation.from_json(json)
# print the JSON string representation of the object
print(IdentityRelation.to_json())

# convert the object into a dict
identity_relation_dict = identity_relation_instance.to_dict()
# create an instance of IdentityRelation from a dict
identity_relation_form_dict = identity_relation.from_dict(identity_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


