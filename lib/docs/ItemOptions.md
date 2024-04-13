# ItemOptions

Item options available to send through connect tokens

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_user_id** | **str** | Client&#39;s identifier for the user, it can be a ID, UUID or even an email. | [optional] 
**webhook_url** | **str** | Url to be notified of this specific item changes | [optional] 

## Example

```python
from pluggy_sdk.models.item_options import ItemOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ItemOptions from a JSON string
item_options_instance = ItemOptions.from_json(json)
# print the JSON string representation of the object
print(ItemOptions.to_json())

# convert the object into a dict
item_options_dict = item_options_instance.to_dict()
# create an instance of ItemOptions from a dict
item_options_from_dict = ItemOptions.from_dict(item_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


