# Connector

Connector object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Primary identifier | 
**name** | **str** | Name of the institution | [optional] 
**institution_url** | **str** | Homepage of the institution | [optional] 
**image_url** | **str** | Image of the logo hosted by Pluggy | [optional] 
**primary_color** | **str** | Primary color | [optional] 
**type** | **str** | Type of institution | [optional] 
**country** | **str** | Country located | [optional] 
**credentials** | [**List[ConnectorCredential]**](ConnectorCredential.md) | Parameters required to start the connection | [optional] 
**has_mfa** | **bool** | Does the connector require an MFA to execute? | [optional] 
**products** | **List[str]** | Products supported by the connector | [optional] 
**oauth** | **bool** | If &#39;true&#39;, the connector requires an Oauth flow to execute | [optional] 
**oauth_url** | **str** | URL to perform Oauth flow if needed | [optional] 
**reset_password_url** | **str** | URL to the financial institution to reset the password | [optional] 
**health** | [**ConnectorHealth**](ConnectorHealth.md) |  | [optional] 
**is_open_finance** | **bool** | Indicates if the connector uses the regulated Open Finance APIs | [optional] 
**supports_payment_initiation** | **bool** | Indicates if the connector supports the payment initiation API | [optional] 

## Example

```python
from pluggy_sdk.models.connector import Connector

# TODO update the JSON string below
json = "{}"
# create an instance of Connector from a JSON string
connector_instance = Connector.from_json(json)
# print the JSON string representation of the object
print(Connector.to_json())

# convert the object into a dict
connector_dict = connector_instance.to_dict()
# create an instance of Connector from a dict
connector_form_dict = connector.from_dict(connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


