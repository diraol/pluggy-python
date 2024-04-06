# WebhooksList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[Webhook]**](Webhook.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.webhooks_list200_response import WebhooksList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksList200Response from a JSON string
webhooks_list200_response_instance = WebhooksList200Response.from_json(json)
# print the JSON string representation of the object
print(WebhooksList200Response.to_json())

# convert the object into a dict
webhooks_list200_response_dict = webhooks_list200_response_instance.to_dict()
# create an instance of WebhooksList200Response from a dict
webhooks_list200_response_form_dict = webhooks_list200_response.from_dict(webhooks_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


