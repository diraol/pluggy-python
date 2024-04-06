# Webhook



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID identifier for the entity | 
**url** | **str** | Url to be notified of item changes | 
**event** | **str** |  | 
**disabled_at** | **datetime** | Date when the webhook was disabled | [optional] 
**created_at** | **datetime** | Date when it was created | [optional] 
**updated_at** | **datetime** | Date of the last update | [optional] 

## Example

```python
from pluggy_sdk.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_form_dict = webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


