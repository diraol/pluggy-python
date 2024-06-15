# PaymentSchedulesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[SchedulePayment]**](SchedulePayment.md) | List of scheduled payments from a payment request | [optional] 

## Example

```python
from pluggy_sdk.models.payment_schedules_list200_response import PaymentSchedulesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSchedulesList200Response from a JSON string
payment_schedules_list200_response_instance = PaymentSchedulesList200Response.from_json(json)
# print the JSON string representation of the object
print(PaymentSchedulesList200Response.to_json())

# convert the object into a dict
payment_schedules_list200_response_dict = payment_schedules_list200_response_instance.to_dict()
# create an instance of PaymentSchedulesList200Response from a dict
payment_schedules_list200_response_from_dict = PaymentSchedulesList200Response.from_dict(payment_schedules_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


