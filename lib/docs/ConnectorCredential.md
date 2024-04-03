# ConnectorCredential

Credential details for a connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the key | 
**label** | **str** | Label for input | 
**type** | **str** | Type of credential required | 
**assistive_text** | **str** | Text to help the user when completing the input | [optional] 
**data** | **str** | Used to return base64 images | [optional] 
**placeholder** | **str** | Placeholder text for the input | [optional] 
**validation** | **str** | Regex validation for the user&#39;s input | [optional] 
**validation_message** | **str** | Validation message when input doesn&#39;t match the regex | [optional] 
**mfa** | **bool** | Credential is an MFA parameter and must be refreshed on each execution | [optional] 
**options** | [**List[CredentialSelectOption]**](CredentialSelectOption.md) | List of possible values for the input | [optional] 

## Example

```python
from openapi_client.models.connector_credential import ConnectorCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorCredential from a JSON string
connector_credential_instance = ConnectorCredential.from_json(json)
# print the JSON string representation of the object
print(ConnectorCredential.to_json())

# convert the object into a dict
connector_credential_dict = connector_credential_instance.to_dict()
# create an instance of ConnectorCredential from a dict
connector_credential_form_dict = connector_credential.from_dict(connector_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


