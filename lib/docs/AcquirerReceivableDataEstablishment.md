# AcquirerReceivableDataEstablishment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_code** | **str** | CNPJ of the company that receives the payment | [optional] 
**company_name** | **str** | Name of the company that receives the payment | [optional] 
**receiving_bank** | **str** | Bank of the receiving account | [optional] 
**agency** | **str** | Agency number of the receiving account | [optional] 
**account** | **str** | Account number of the receiving account (with check digit) | [optional] 

## Example

```python
from openapi_client.models.acquirer_receivable_data_establishment import AcquirerReceivableDataEstablishment

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerReceivableDataEstablishment from a JSON string
acquirer_receivable_data_establishment_instance = AcquirerReceivableDataEstablishment.from_json(json)
# print the JSON string representation of the object
print(AcquirerReceivableDataEstablishment.to_json())

# convert the object into a dict
acquirer_receivable_data_establishment_dict = acquirer_receivable_data_establishment_instance.to_dict()
# create an instance of AcquirerReceivableDataEstablishment from a dict
acquirer_receivable_data_establishment_form_dict = acquirer_receivable_data_establishment.from_dict(acquirer_receivable_data_establishment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


