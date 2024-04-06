# WebhookCreationErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from pluggy_sdk.models.webhook_creation_error_response import WebhookCreationErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreationErrorResponse from a JSON string
webhook_creation_error_response_instance = WebhookCreationErrorResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookCreationErrorResponse.to_json())

# convert the object into a dict
webhook_creation_error_response_dict = webhook_creation_error_response_instance.to_dict()
# create an instance of WebhookCreationErrorResponse from a dict
webhook_creation_error_response_form_dict = webhook_creation_error_response.from_dict(webhook_creation_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


