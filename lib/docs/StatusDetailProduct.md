# StatusDetailProduct

Detailed status of the product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_at** | **datetime** | Date when the product was last updated | [optional] 
**is_updated** | **bool** | Product was updated in the last execution | [optional] 
**warnings** | [**List[StatusDetailProductWarning]**](StatusDetailProductWarning.md) | Warnings about the product data. For example, a warning about missing permissions for viewing a product | [optional] 

## Example

```python
from pluggy_sdk.models.status_detail_product import StatusDetailProduct

# TODO update the JSON string below
json = "{}"
# create an instance of StatusDetailProduct from a JSON string
status_detail_product_instance = StatusDetailProduct.from_json(json)
# print the JSON string representation of the object
print(StatusDetailProduct.to_json())

# convert the object into a dict
status_detail_product_dict = status_detail_product_instance.to_dict()
# create an instance of StatusDetailProduct from a dict
status_detail_product_from_dict = StatusDetailProduct.from_dict(status_detail_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


