# AcquirerSaleInstallment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** | Ordinal number of the installment | [optional] 
**net_amount** | **float** | Amount of the installment, with taxes applied | [optional] 
**receipt_date** | **datetime** | Date when the installment was received | [optional] 

## Example

```python
from pluggy_sdk.models.acquirer_sale_installment import AcquirerSaleInstallment

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerSaleInstallment from a JSON string
acquirer_sale_installment_instance = AcquirerSaleInstallment.from_json(json)
# print the JSON string representation of the object
print(AcquirerSaleInstallment.to_json())

# convert the object into a dict
acquirer_sale_installment_dict = acquirer_sale_installment_instance.to_dict()
# create an instance of AcquirerSaleInstallment from a dict
acquirer_sale_installment_from_dict = AcquirerSaleInstallment.from_dict(acquirer_sale_installment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


