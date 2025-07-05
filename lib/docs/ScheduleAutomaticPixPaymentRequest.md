# ScheduleAutomaticPixPaymentRequest

Request to schedule an Automatic PIX payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Transaction value | 
**description** | **str** | Transaction description | [optional] 
**var_date** | **date** | The payment date, which must fall between D+2 and D+10. Date format must be YYYY-MM-DD (for example: 2025-06-16) | 
**client_payment_id** | **str** | External identifier for the payment | [optional] 

## Example

```python
from pluggy_sdk.models.schedule_automatic_pix_payment_request import ScheduleAutomaticPixPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAutomaticPixPaymentRequest from a JSON string
schedule_automatic_pix_payment_request_instance = ScheduleAutomaticPixPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleAutomaticPixPaymentRequest.to_json())

# convert the object into a dict
schedule_automatic_pix_payment_request_dict = schedule_automatic_pix_payment_request_instance.to_dict()
# create an instance of ScheduleAutomaticPixPaymentRequest from a dict
schedule_automatic_pix_payment_request_from_dict = ScheduleAutomaticPixPaymentRequest.from_dict(schedule_automatic_pix_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


