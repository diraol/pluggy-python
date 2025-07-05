# AutomaticPixPayment

Automatic PIX payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Payment primary identifier | 
**status** | **str** | Payment status | 
**amount** | **float** | Payment amount | 
**description** | **str** | Payment description | [optional] 
**var_date** | **date** | Payment scheduled date | 
**end_to_end_id** | **str** | Payment end to end identifier | [optional] 
**error_detail** | [**SchedulePaymentErrorDetail**](SchedulePaymentErrorDetail.md) |  | [optional] 
**client_payment_id** | **str** | External identifier for the payment | [optional] 

## Example

```python
from pluggy_sdk.models.automatic_pix_payment import AutomaticPixPayment

# TODO update the JSON string below
json = "{}"
# create an instance of AutomaticPixPayment from a JSON string
automatic_pix_payment_instance = AutomaticPixPayment.from_json(json)
# print the JSON string representation of the object
print(AutomaticPixPayment.to_json())

# convert the object into a dict
automatic_pix_payment_dict = automatic_pix_payment_instance.to_dict()
# create an instance of AutomaticPixPayment from a dict
automatic_pix_payment_from_dict = AutomaticPixPayment.from_dict(automatic_pix_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


