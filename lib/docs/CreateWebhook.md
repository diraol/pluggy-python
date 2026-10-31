# CreateWebhook



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Public https url that will receive the POST of the event. It must use the default port (443), can&#39;t include a username or password, can&#39;t be longer than 2048 characters, and its host must be a domain name (not an IP address, localhost or an internal name) that resolves only to public IP addresses. | 
**event** | [**WebhookEventType**](WebhookEventType.md) |  | 
**headers** | **object** | HTTP headers that will be included in the webhook notifications (useful for things like authorization) | [optional] 

## Example

```python
from pluggy_sdk.models.create_webhook import CreateWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhook from a JSON string
create_webhook_instance = CreateWebhook.from_json(json)
# print the JSON string representation of the object
print(CreateWebhook.to_json())

# convert the object into a dict
create_webhook_dict = create_webhook_instance.to_dict()
# create an instance of CreateWebhook from a dict
create_webhook_from_dict = CreateWebhook.from_dict(create_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


