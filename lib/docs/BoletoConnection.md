# BoletoConnection

Response with information related to a boleto connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**connector_id** | **int** | Primary identifier of the connector associated with this connection | 
**created_at** | **datetime** | Date when the connection was created | 
**updated_at** | **datetime** | Date when the connection was last updated | 

## Example

```python
from pluggy_sdk.models.boleto_connection import BoletoConnection

# TODO update the JSON string below
json = "{}"
# create an instance of BoletoConnection from a JSON string
boleto_connection_instance = BoletoConnection.from_json(json)
# print the JSON string representation of the object
print(BoletoConnection.to_json())

# convert the object into a dict
boleto_connection_dict = boleto_connection_instance.to_dict()
# create an instance of BoletoConnection from a dict
boleto_connection_from_dict = BoletoConnection.from_dict(boleto_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


