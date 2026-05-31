# AutomaticPixPaymentAttempt

Payment attempt. It represents an attempt to complete this payment. Useful for tracking the payment history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Attempt primary identifier | 
**status** | **str** | Attempt status | 
**end_to_end_id** | **str** | Attempt end to end identifier | [optional] 
**var_date** | **date** | Attempt date | 
**error_detail** | [**AutomaticPixPaymentErrorDetail**](AutomaticPixPaymentErrorDetail.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.automatic_pix_payment_attempt import AutomaticPixPaymentAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of AutomaticPixPaymentAttempt from a JSON string
automatic_pix_payment_attempt_instance = AutomaticPixPaymentAttempt.from_json(json)
# print the JSON string representation of the object
print(AutomaticPixPaymentAttempt.to_json())

# convert the object into a dict
automatic_pix_payment_attempt_dict = automatic_pix_payment_attempt_instance.to_dict()
# create an instance of AutomaticPixPaymentAttempt from a dict
automatic_pix_payment_attempt_from_dict = AutomaticPixPaymentAttempt.from_dict(automatic_pix_payment_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


