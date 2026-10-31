# ItemOptions

Item options available to send through connect tokens

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_user_id** | **str** | Client&#39;s external identifier for the user, it can be a ID, UUID or even an email. This is free for clients to use. | [optional] 
**webhook_url** | **str** | Public https url to be notified of this specific item changes. Same rules as the &#x60;url&#x60; of a webhook: default port (443) only, no username or password, at most 2048 characters, and a domain name (not an IP address, localhost or an internal name) that resolves only to public IP addresses. Otherwise the request fails with 400. | [optional] 
**oauth_redirect_uri** | **str** | Url to redirect the user after the connect flow | [optional] 
**avoid_duplicates** | **bool** | Avoids creating a new item if there is already one with the same credentials | [optional] 
**products** | **List[str]** | Products to be collected in items created or updated with this connect token. Used only when the item request doesn&#39;t send its own products. | [optional] 

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


