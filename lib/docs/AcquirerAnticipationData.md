# AcquirerAnticipationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**net_amount** | **float** | Net amount of the anticipation | 
**fee** | **float** | Percentage of monthly fee (e.g 1.5 &#x3D; 1.5%) | 
**fee_amount** | **float** | Fee amount | 

## Example

```python
from openapi_client.models.acquirer_anticipation_data import AcquirerAnticipationData

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerAnticipationData from a JSON string
acquirer_anticipation_data_instance = AcquirerAnticipationData.from_json(json)
# print the JSON string representation of the object
print(AcquirerAnticipationData.to_json())

# convert the object into a dict
acquirer_anticipation_data_dict = acquirer_anticipation_data_instance.to_dict()
# create an instance of AcquirerAnticipationData from a dict
acquirer_anticipation_data_form_dict = acquirer_anticipation_data.from_dict(acquirer_anticipation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


