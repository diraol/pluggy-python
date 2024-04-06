# CreateItemParameters

Connector's credentials that are required to execute on a Key-Value object or a string if they are encrypted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from pluggy_sdk.models.create_item_parameters import CreateItemParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateItemParameters from a JSON string
create_item_parameters_instance = CreateItemParameters.from_json(json)
# print the JSON string representation of the object
print(CreateItemParameters.to_json())

# convert the object into a dict
create_item_parameters_dict = create_item_parameters_instance.to_dict()
# create an instance of CreateItemParameters from a dict
create_item_parameters_form_dict = create_item_parameters.from_dict(create_item_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


