# StatusDetail

Detailed status of the item. This field will be present when the status is PARTIAL_SUCCESS or when a product in the item has warnings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**credit_cards** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**transactions** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**investments** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**identity** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**investment_transactions** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**payment_data** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**income_reports** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**loans** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**portfolio** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 
**opportunities** | [**StatusDetailProduct**](StatusDetailProduct.md) |  | [optional] 

## Example

```python
from openapi_client.models.status_detail import StatusDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StatusDetail from a JSON string
status_detail_instance = StatusDetail.from_json(json)
# print the JSON string representation of the object
print(StatusDetail.to_json())

# convert the object into a dict
status_detail_dict = status_detail_instance.to_dict()
# create an instance of StatusDetail from a dict
status_detail_form_dict = status_detail.from_dict(status_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


