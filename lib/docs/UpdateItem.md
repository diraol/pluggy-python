# UpdateItem

Update Item Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**UpdateItemParameters**](UpdateItemParameters.md) |  | [optional] 
**client_user_id** | **str** | Client&#39;s external identifier for the user, it can be a ID, UUID or even an email. This is free for clients to use. | [optional] 
**webhook_url** | **str** | Public https url to be notified of item changes. Same rules as the &#x60;url&#x60; of a webhook: default port (443) only, no username or password, at most 2048 characters, and a domain name (not an IP address, localhost or an internal name) that resolves only to public IP addresses. Otherwise the request fails with 400. | [optional] 
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
update_item_from_dict = UpdateItem.from_dict(update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


