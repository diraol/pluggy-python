# CreateWebhook



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**event** | **str** |  | 
**headers** | **object** | HTTP headers that will be included in the webhook notifications (useful for things like authorization) | [optional] 

## Example

```python
from openapi_client.models.create_webhook import CreateWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhook from a JSON string
create_webhook_instance = CreateWebhook.from_json(json)
# print the JSON string representation of the object
print(CreateWebhook.to_json())

# convert the object into a dict
create_webhook_dict = create_webhook_instance.to_dict()
# create an instance of CreateWebhook from a dict
create_webhook_form_dict = create_webhook.from_dict(create_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


