# AcquirerSaleInstallmentData

Acquirer Sale product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** | Ordinal number of the installment | 
**gross_amount** | **float** | Gross amount of the installment | 
**net_amount** | **float** | Net amount of the installment, with taxes applied | [optional] 
**receipt_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.acquirer_sale_installment_data import AcquirerSaleInstallmentData

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerSaleInstallmentData from a JSON string
acquirer_sale_installment_data_instance = AcquirerSaleInstallmentData.from_json(json)
# print the JSON string representation of the object
print(AcquirerSaleInstallmentData.to_json())

# convert the object into a dict
acquirer_sale_installment_data_dict = acquirer_sale_installment_data_instance.to_dict()
# create an instance of AcquirerSaleInstallmentData from a dict
acquirer_sale_installment_data_form_dict = acquirer_sale_installment_data.from_dict(acquirer_sale_installment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


