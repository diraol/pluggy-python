# ConnectorUserAction

User action details for an item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instructions** | **str** | Instructions related to the user action | 
**attributes** | **object** | &#39;{ [key]:[value] }&#39;. Additional information related to the user action, for exampke in some device authorization flow | [optional] 
**expires_at** | **datetime** | User action expiration date | [optional] 

## Example

```python
from pluggy_sdk.models.connector_user_action import ConnectorUserAction

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorUserAction from a JSON string
connector_user_action_instance = ConnectorUserAction.from_json(json)
# print the JSON string representation of the object
print(ConnectorUserAction.to_json())

# convert the object into a dict
connector_user_action_dict = connector_user_action_instance.to_dict()
# create an instance of ConnectorUserAction from a dict
connector_user_action_form_dict = connector_user_action.from_dict(connector_user_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


