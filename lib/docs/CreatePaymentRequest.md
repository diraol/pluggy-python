# CreatePaymentRequest

Request with information to create a payment request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Requested amount | 
**description** | **str** | Payment description | [optional] 
**callback_urls** | [**PaymentRequestCallbackUrls**](PaymentRequestCallbackUrls.md) |  | [optional] 
**recipient_id** | **str** | Payment receiver identifier | [optional] 
**customer_id** | **str** | Customer identifier associated to the payment | [optional] 
**client_payment_id** | **str** | Your payment identifier | [optional] 
**schedule** | [**CreatePaymentRequestSchedule**](CreatePaymentRequestSchedule.md) |  | [optional] 
**is_sandbox** | **bool** | Indicates if this payment request should be created in sandbox mode. Default: false. | [optional] [default to False]

## Example

```python
from pluggy_sdk.models.create_payment_request import CreatePaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentRequest from a JSON string
create_payment_request_instance = CreatePaymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentRequest.to_json())

# convert the object into a dict
create_payment_request_dict = create_payment_request_instance.to_dict()
# create an instance of CreatePaymentRequest from a dict
create_payment_request_from_dict = CreatePaymentRequest.from_dict(create_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


