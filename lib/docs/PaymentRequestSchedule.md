# PaymentRequestSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Schedule discriminator. Always &#x60;SINGLE&#x60; for this variant. | 
**var_date** | **date** | Settlement date for the payment (YYYY-MM-DD). | 
**start_date** | **date** | The start date of the validity of the scheduled payment authorization. | 
**occurrences** | **float** | Under the specified schedule frequency, how many payments will be scheduled to occur. | 
**day_of_week** | **str** | Day of the week on which each payment will occur. For instance, if set to &#x60;MONDAY&#x60;, the first payment will occur on the first Monday after &#x60;startDate&#x60; (or the same day, if it is already Monday), and every Monday after that. | 
**day_of_month** | **float** | Day of the month on which each payment will occur. For example, if &#x60;10&#x60;, the first payment will occur on the next 10th day of the month after &#x60;startDate&#x60; (or the same day if it is already the 10th), and every 10th day after that. | 
**dates** | **List[date]** | Explicit list of dates (YYYY-MM-DD) on which payments will be settled. | 
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


