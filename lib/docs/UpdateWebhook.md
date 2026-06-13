# UpdateWebhook

Partial update of a webhook. All fields are optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | New https url that will receive the POST of the event | [optional] 
**event** | [**WebhookEventType**](WebhookEventType.md) | New event the webhook should listen to | [optional] 
**headers** | **object** | HTTP headers to include in webhook notifications. Send null to clear the existing headers. | [optional] 
**enabled** | **bool** | Re-enable a webhook that was previously disabled. When set to true, clears the disabledAt timestamp. | [optional] 

## Example

```python
from pluggy_sdk.models.update_webhook import UpdateWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhook from a JSON string
update_webhook_instance = UpdateWebhook.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhook.to_json())

# convert the object into a dict
update_webhook_dict = update_webhook_instance.to_dict()
# create an instance of UpdateWebhook from a dict
update_webhook_from_dict = UpdateWebhook.from_dict(update_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


