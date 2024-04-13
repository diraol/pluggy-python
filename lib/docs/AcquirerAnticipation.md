# AcquirerAnticipation

Acquirer Anticipation product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier of the acquirer anticipation | 
**item_id** | **str** | Primary identifier of the item associated to the acquirer anticipation | 
**description** | **str** | Clean description of the acquirer anticipation | 
**currency_code** | **str** | Currency ISO code | 
**var_date** | **datetime** | Date when the acquirer anticipation was requested | 
**gross_amount** | **float** | Acquirer anticipation gross amount | 
**status** | **str** | Status of the payment anticipation | [optional] 
**net_amount** | **float** | Acquirer anticipation net amount | [optional] 
**fee** | **float** | Percentage of monthly fee (e.g 1.5 &#x3D; 1.5%) | [optional] 
**fee_amount** | **float** | Fee amount | [optional] 

## Example

```python
from pluggy_sdk.models.acquirer_anticipation import AcquirerAnticipation

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerAnticipation from a JSON string
acquirer_anticipation_instance = AcquirerAnticipation.from_json(json)
# print the JSON string representation of the object
print(AcquirerAnticipation.to_json())

# convert the object into a dict
acquirer_anticipation_dict = acquirer_anticipation_instance.to_dict()
# create an instance of AcquirerAnticipation from a dict
acquirer_anticipation_from_dict = AcquirerAnticipation.from_dict(acquirer_anticipation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


