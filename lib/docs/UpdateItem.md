# UpdateItem

Update Item Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**UpdateItemParameters**](UpdateItemParameters.md) |  | [optional] 
**client_user_id** | **str** | Client&#39;s identifier for the user, it can be a ID, UUID or even an email. | [optional] 
**webhook_url** | **str** | Url to be notified of item changes | [optional] 
**products** | **List[str]** | Products to be collected in the connection | [optional] 

## Example

```python
from pluggy_sdk.models.update_item import UpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateItem from a JSON string
update_item_instance = UpdateItem.from_json(json)
# print the JSON string representation of the object
print(UpdateItem.to_json())

# convert the object into a dict
update_item_dict = update_item_instance.to_dict()
# create an instance of UpdateItem from a dict
update_item_form_dict = update_item.from_dict(update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


