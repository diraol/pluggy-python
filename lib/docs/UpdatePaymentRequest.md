# UpdatePaymentRequest

Request with information to update a payment request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Requested amount | [optional] 
**description** | **str** | Payment description | [optional] 
**callback_urls** | [**PaymentRequestCallbackUrls**](PaymentRequestCallbackUrls.md) |  | [optional] 
**recipient_id** | **str** | Payment receiver identifier | [optional] 
**customer_id** | **str** | Customer identifier associated to the payment | [optional] 
**client_payment_id** | **str** | Your payment identifier | [optional] 
**is_sandbox** | **bool** | Indicates if this payment request should be updated as sandbox. Default: false. | [optional] [default to False]

## Example

```python
from pluggy_sdk.models.update_payment_request import UpdatePaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentRequest from a JSON string
update_payment_request_instance = UpdatePaymentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentRequest.to_json())

# convert the object into a dict
update_payment_request_dict = update_payment_request_instance.to_dict()
# create an instance of UpdatePaymentRequest from a dict
update_payment_request_from_dict = UpdatePaymentRequest.from_dict(update_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


