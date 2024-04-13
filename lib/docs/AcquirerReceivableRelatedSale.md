# AcquirerReceivableRelatedSale

Acquirer receivable related operation (sale or cancellation)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date when the sale occurred | 
**gross_amount** | **float** | Gross amount of the related sale | 
**net_amount** | **float** | Net amount of the related sale | 
**installment_count** | **float** | Amount of installments of the sale | 
**installment_number** | **float** | Installment of the sale being paid or cancelled | 
**nsu** | **str** | NSU of the sale | 

## Example

```python
from pluggy_sdk.models.acquirer_receivable_related_sale import AcquirerReceivableRelatedSale

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerReceivableRelatedSale from a JSON string
acquirer_receivable_related_sale_instance = AcquirerReceivableRelatedSale.from_json(json)
# print the JSON string representation of the object
print(AcquirerReceivableRelatedSale.to_json())

# convert the object into a dict
acquirer_receivable_related_sale_dict = acquirer_receivable_related_sale_instance.to_dict()
# create an instance of AcquirerReceivableRelatedSale from a dict
acquirer_receivable_related_sale_from_dict = AcquirerReceivableRelatedSale.from_dict(acquirer_receivable_related_sale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


