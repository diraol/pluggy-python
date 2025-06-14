# RetryAutomaticPixPaymentRequest

Request to retry an automatic PIX payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date to retry the payment within a 7-day window. Date format must be YYYY-MM-DD (for example: 2025-06-16) | 

## Example

```python
from pluggy_sdk.models.retry_automatic_pix_payment_request import RetryAutomaticPixPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetryAutomaticPixPaymentRequest from a JSON string
retry_automatic_pix_payment_request_instance = RetryAutomaticPixPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(RetryAutomaticPixPaymentRequest.to_json())

# convert the object into a dict
retry_automatic_pix_payment_request_dict = retry_automatic_pix_payment_request_instance.to_dict()
# create an instance of RetryAutomaticPixPaymentRequest from a dict
retry_automatic_pix_payment_request_from_dict = RetryAutomaticPixPaymentRequest.from_dict(retry_automatic_pix_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


