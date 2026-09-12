# ScrValidationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codigo** | **str** |  | [optional] 
**mensagem** | **str** |  | [optional] 

## Example

```python
from pluggy_sdk.models.scr_validation_message import ScrValidationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ScrValidationMessage from a JSON string
scr_validation_message_instance = ScrValidationMessage.from_json(json)
# print the JSON string representation of the object
print(ScrValidationMessage.to_json())

# convert the object into a dict
scr_validation_message_dict = scr_validation_message_instance.to_dict()
# create an instance of ScrValidationMessage from a dict
scr_validation_message_from_dict = ScrValidationMessage.from_dict(scr_validation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


