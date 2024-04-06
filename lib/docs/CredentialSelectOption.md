# CredentialSelectOption

Option for ConnectorCredential of type select

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value for the option | 
**label** | **str** | Label for the option | 

## Example

```python
from pluggy_sdk.models.credential_select_option import CredentialSelectOption

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSelectOption from a JSON string
credential_select_option_instance = CredentialSelectOption.from_json(json)
# print the JSON string representation of the object
print(CredentialSelectOption.to_json())

# convert the object into a dict
credential_select_option_dict = credential_select_option_instance.to_dict()
# create an instance of CredentialSelectOption from a dict
credential_select_option_form_dict = credential_select_option.from_dict(credential_select_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


