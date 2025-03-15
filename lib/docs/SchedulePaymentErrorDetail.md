# SchedulePaymentErrorDetail

Details about an error that occurred with the scheduled payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code | [optional] 
**description** | **str** | Human-readable description of the error | [optional] 
**detail** | **str** | Additional details about the error in the provider&#39;s language | [optional] 

## Example

```python
from pluggy_sdk.models.schedule_payment_error_detail import SchedulePaymentErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePaymentErrorDetail from a JSON string
schedule_payment_error_detail_instance = SchedulePaymentErrorDetail.from_json(json)
# print the JSON string representation of the object
print(SchedulePaymentErrorDetail.to_json())

# convert the object into a dict
schedule_payment_error_detail_dict = schedule_payment_error_detail_instance.to_dict()
# create an instance of SchedulePaymentErrorDetail from a dict
schedule_payment_error_detail_from_dict = SchedulePaymentErrorDetail.from_dict(schedule_payment_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


