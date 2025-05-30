# SchedulePayment

Information of a schedule payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** | Scheduled payment description | 
**status** | **str** | Scheduled payment status | 
**scheduled_date** | **date** | Date when the payment is scheduled | 
**end_to_end_id** | **str** | Identifier for the payment, used to link the scheduled payment with the corresponding payment received | [optional] 
**error_detail** | [**SchedulePaymentErrorDetail**](SchedulePaymentErrorDetail.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.schedule_payment import SchedulePayment

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePayment from a JSON string
schedule_payment_instance = SchedulePayment.from_json(json)
# print the JSON string representation of the object
print(SchedulePayment.to_json())

# convert the object into a dict
schedule_payment_dict = schedule_payment_instance.to_dict()
# create an instance of SchedulePayment from a dict
schedule_payment_from_dict = SchedulePayment.from_dict(schedule_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


