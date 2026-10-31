# CreateItem

Create Item Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **float** | Primary identifier of the connector | 
**parameters** | [**CreateItemParameters**](CreateItemParameters.md) |  | 
**webhook_url** | **str** | Public https url to be notified of item changes. Same rules as the &#x60;url&#x60; of a webhook: default port (443) only, no username or password, at most 2048 characters, and a domain name (not an IP address, localhost or an internal name) that resolves only to public IP addresses. Otherwise the request fails with 400. | [optional] 
**client_user_id** | **str** | Client&#39;s external identifier for the user, it can be a ID, UUID or even an email. This is free for clients to use. | [optional] 
**oauth_redirect_uri** | **str** | Redirect URI required for the Oauth flow | [optional] 
**products** | **List[str]** | Products to be collected in the connection | [optional] 
**avoid_duplicates** | **bool** | Avoids creating a new item if there is already one with the same credentials | [optional] 

## Example

```python
from pluggy_sdk.models.create_item import CreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateItem from a JSON string
create_item_instance = CreateItem.from_json(json)
# print the JSON string representation of the object
print(CreateItem.to_json())

# convert the object into a dict
create_item_dict = create_item_instance.to_dict()
# create an instance of CreateItem from a dict
create_item_from_dict = CreateItem.from_dict(create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


