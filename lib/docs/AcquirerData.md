# AcquirerData

Data of a transaction specific to institutions of type PAYMENT_ACCOUNT (acquiring banks)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of acquiring bank transaction | 
**sale_data** | [**AcquirerSaleData**](AcquirerSaleData.md) |  | [optional] 
**receivable_data** | [**AcquirerReceivableData**](AcquirerReceivableData.md) |  | [optional] 
**anticipation_data** | [**AcquirerAnticipationData**](AcquirerAnticipationData.md) |  | [optional] 

## Example

```python
from openapi_client.models.acquirer_data import AcquirerData

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerData from a JSON string
acquirer_data_instance = AcquirerData.from_json(json)
# print the JSON string representation of the object
print(AcquirerData.to_json())

# convert the object into a dict
acquirer_data_dict = acquirer_data_instance.to_dict()
# create an instance of AcquirerData from a dict
acquirer_data_form_dict = acquirer_data.from_dict(acquirer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


