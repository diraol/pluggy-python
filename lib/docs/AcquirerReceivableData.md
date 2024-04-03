# AcquirerReceivableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_status** | **str** |  | [optional] 
**card_flag** | **str** |  | [optional] 
**establishment** | [**AcquirerReceivableDataEstablishment**](AcquirerReceivableDataEstablishment.md) |  | [optional] 
**net_amount** | **float** | Net amount of the receivable | [optional] 

## Example

```python
from openapi_client.models.acquirer_receivable_data import AcquirerReceivableData

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerReceivableData from a JSON string
acquirer_receivable_data_instance = AcquirerReceivableData.from_json(json)
# print the JSON string representation of the object
print(AcquirerReceivableData.to_json())

# convert the object into a dict
acquirer_receivable_data_dict = acquirer_receivable_data_instance.to_dict()
# create an instance of AcquirerReceivableData from a dict
acquirer_receivable_data_form_dict = acquirer_receivable_data.from_dict(acquirer_receivable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


