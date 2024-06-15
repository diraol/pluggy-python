# PaymentRequestSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**var_date** | **date** |  | 
**start_date** | **date** |  | 
**quantity** | **float** |  | 
**day_of_week** | **str** | Day of the week to generate the payment | 
**day_of_month** | **float** | Day of the mont to generate the payment | 
**dates** | **List[date]** |  | 
**additional_information** | **str** | Additional information about the custom schedule | [optional] 

## Example

```python
from pluggy_sdk.models.payment_request_schedule import PaymentRequestSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestSchedule from a JSON string
payment_request_schedule_instance = PaymentRequestSchedule.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestSchedule.to_json())

# convert the object into a dict
payment_request_schedule_dict = payment_request_schedule_instance.to_dict()
# create an instance of PaymentRequestSchedule from a dict
payment_request_schedule_from_dict = PaymentRequestSchedule.from_dict(payment_request_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


