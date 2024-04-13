# BulkPayment

Response with information related to a bulk payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**total_amount** | **float** | Total amount of all requests associated with the bulk payment | 
**status** | **str** | Bulk payment status | 
**created_at** | **datetime** | Date when the payment request was created | 
**updated_at** | **datetime** | Date when the payment request was updated | 
**callback_urls** | [**PaymentRequestCallbackUrls**](PaymentRequestCallbackUrls.md) |  | [optional] 
**payment_url** | **str** | URL to begin the payment intent creation flow for this payment request | 
**payment_requests** | [**List[PaymentRequest]**](PaymentRequest.md) | List of payment requests associated with the bulk payment | 
**smart_account** | [**SmartAccount**](SmartAccount.md) |  | 

## Example

```python
from pluggy_sdk.models.bulk_payment import BulkPayment

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPayment from a JSON string
bulk_payment_instance = BulkPayment.from_json(json)
# print the JSON string representation of the object
print(BulkPayment.to_json())

# convert the object into a dict
bulk_payment_dict = bulk_payment_instance.to_dict()
# create an instance of BulkPayment from a dict
bulk_payment_from_dict = BulkPayment.from_dict(bulk_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


