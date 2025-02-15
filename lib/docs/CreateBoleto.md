# CreateBoleto

Request with information to create a boleto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boleto_connection_id** | **str** | Primary identifier of the boleto connection | 
**boleto** | [**CreateBoletoBoleto**](CreateBoletoBoleto.md) |  | 

## Example

```python
from pluggy_sdk.models.create_boleto import CreateBoleto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBoleto from a JSON string
create_boleto_instance = CreateBoleto.from_json(json)
# print the JSON string representation of the object
print(CreateBoleto.to_json())

# convert the object into a dict
create_boleto_dict = create_boleto_instance.to_dict()
# create an instance of CreateBoleto from a dict
create_boleto_from_dict = CreateBoleto.from_dict(create_boleto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


