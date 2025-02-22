# CreateBoletoConnectionFromItem

Request with information to create a boleto connection from an Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Item ID | 

## Example

```python
from pluggy_sdk.models.create_boleto_connection_from_item import CreateBoletoConnectionFromItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBoletoConnectionFromItem from a JSON string
create_boleto_connection_from_item_instance = CreateBoletoConnectionFromItem.from_json(json)
# print the JSON string representation of the object
print(CreateBoletoConnectionFromItem.to_json())

# convert the object into a dict
create_boleto_connection_from_item_dict = create_boleto_connection_from_item_instance.to_dict()
# create an instance of CreateBoletoConnectionFromItem from a dict
create_boleto_connection_from_item_from_dict = CreateBoletoConnectionFromItem.from_dict(create_boleto_connection_from_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


