# CreateItem

Create Item Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **float** | Primary identifier of the connector | 
**parameters** | [**CreateItemParameters**](CreateItemParameters.md) |  | 
**webhook_url** | **str** | Url to be notified of item changes | [optional] 
**client_user_id** | **str** | Client&#39;s identifier for the user, it can be a ID, UUID or even an email. | [optional] 
**products** | **List[str]** | Products to be collected in the connection | [optional] 

## Example

```python
from openapi_client.models.create_item import CreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateItem from a JSON string
create_item_instance = CreateItem.from_json(json)
# print the JSON string representation of the object
print(CreateItem.to_json())

# convert the object into a dict
create_item_dict = create_item_instance.to_dict()
# create an instance of CreateItem from a dict
create_item_form_dict = create_item.from_dict(create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


