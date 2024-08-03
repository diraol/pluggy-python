# SmartTransferCallbackUrls

Redirect urls after the preauthorization flow was completed or ended in error status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **str** | Url to be redirected after the preauthorization was completed | [optional] 
**error** | **str** | Url to be redirected after the preauthorization ended in error status | [optional] 

## Example

```python
from pluggy_sdk.models.smart_transfer_callback_urls import SmartTransferCallbackUrls

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferCallbackUrls from a JSON string
smart_transfer_callback_urls_instance = SmartTransferCallbackUrls.from_json(json)
# print the JSON string representation of the object
print(SmartTransferCallbackUrls.to_json())

# convert the object into a dict
smart_transfer_callback_urls_dict = smart_transfer_callback_urls_instance.to_dict()
# create an instance of SmartTransferCallbackUrls from a dict
smart_transfer_callback_urls_from_dict = SmartTransferCallbackUrls.from_dict(smart_transfer_callback_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


