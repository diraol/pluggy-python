# UpdateItemParameters

Parameters to update on the item stored credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from pluggy_sdk.models.update_item_parameters import UpdateItemParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateItemParameters from a JSON string
update_item_parameters_instance = UpdateItemParameters.from_json(json)
# print the JSON string representation of the object
print(UpdateItemParameters.to_json())

# convert the object into a dict
update_item_parameters_dict = update_item_parameters_instance.to_dict()
# create an instance of UpdateItemParameters from a dict
update_item_parameters_from_dict = UpdateItemParameters.from_dict(update_item_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


