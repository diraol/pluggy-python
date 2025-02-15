# CreateBoletoConnection

Request with information to create a boleto connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **int** | Connector identifier. Check out the list of connectors, and if it has the flag &#39;supportsBoletoManagement&#39; as true, it means it&#39;s possible to create a boleto connection with it. | 
**credentials** | **Dict[str, str]** | Credentials required for the connection. For Inter, they are clientId, clientSecret, certificate and privateKey, follow: https://docs.pluggy.ai/docs/connect-an-account#inter-pj | 

## Example

```python
from pluggy_sdk.models.create_boleto_connection import CreateBoletoConnection

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBoletoConnection from a JSON string
create_boleto_connection_instance = CreateBoletoConnection.from_json(json)
# print the JSON string representation of the object
print(CreateBoletoConnection.to_json())

# convert the object into a dict
create_boleto_connection_dict = create_boleto_connection_instance.to_dict()
# create an instance of CreateBoletoConnection from a dict
create_boleto_connection_from_dict = CreateBoletoConnection.from_dict(create_boleto_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


