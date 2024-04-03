# Item

Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**connector** | [**Connector**](Connector.md) |  | [optional] 
**status** | **str** | Status of the Item | 
**execution_status** | **str** | Status of the sync execution | 
**error** | [**ItemError**](ItemError.md) |  | [optional] 
**parameter** | [**ConnectorCredential**](ConnectorCredential.md) |  | [optional] 
**user_action** | [**ConnectorUserAction**](ConnectorUserAction.md) |  | [optional] 
**webhook_url** | **str** | Url to be notified of item changes | [optional] 
**created_at** | **datetime** | Date of creation | [optional] 
**updated_at** | **datetime** | Date of last modification | [optional] 
**last_updated_at** | **datetime** | Date of last syncronization | [optional] 
**status_detail** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**next_auto_sync_at** | **datetime** | Date of next auto-sync, or null if auto-sync is disabled for this Item | [optional] 
**consecutive_failed_login_attempts** | **float** | Consecutives execution that ends up with a LOGIN_ERROR status | [optional] 
**products** | **List[str]** | Products collected by the item | [optional] 

## Example

```python
from openapi_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_form_dict = item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


