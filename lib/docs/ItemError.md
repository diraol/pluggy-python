# ItemError

Detailed error message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code | 
**message** | **str** | Detailed error message | 
**provider_message** | **str** | Information provider by the institution mainly when user needs to perform an action | [optional] 
**attributes** | **object** | &#39;{ [key]:[value] }&#39;. Additional information necessary for future executions, used for example in some device authorization flow | [optional] 

## Example

```python
from openapi_client.models.item_error import ItemError

# TODO update the JSON string below
json = "{}"
# create an instance of ItemError from a JSON string
item_error_instance = ItemError.from_json(json)
# print the JSON string representation of the object
print(ItemError.to_json())

# convert the object into a dict
item_error_dict = item_error_instance.to_dict()
# create an instance of ItemError from a dict
item_error_form_dict = item_error.from_dict(item_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


