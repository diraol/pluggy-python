# AutomaticPixPaymentAttempt

Payment attempt. It represents an attempt to complete this payment. Useful for tracking the payment history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Attempt primary identifier | 
**status** | **str** | Attempt status. Each attempt has an independent lifecycle within the parent payment. - &#x60;IN_PROGRESS&#x60;: the attempt was submitted and is awaiting confirmation. - &#x60;COMPLETED&#x60;: the attempt was confirmed (the parent payment also becomes &#x60;COMPLETED&#x60;). - &#x60;CANCELED&#x60;: the attempt was canceled. - &#x60;ERROR&#x60;: the attempt failed (see &#x60;errorDetail&#x60;). The parent payment may be retried with a new attempt. | 
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


