# CreatePaymentIntent

Request with information to create a payment intent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_request_id** | **str** | Primary identifier of the payment request associated to the payment intent | [optional] 
**bulk_payment_id** | **str** | Primary identifier of the bulk payment associated to the payment intent | [optional] 
**parameters** | [**PaymentIntentParameter**](PaymentIntentParameter.md) |  | [optional] 
**connector_id** | **float** | Primary identifier of the connector associated to the payment intent | [optional] 
**payment_method** | **str** | Payment method can be PIS (Payment Initiation) or PIX (PIX QR flow), if PIX selected &#x60;bulkPaymentId&#x60; or a &#x60;paymentRequest&#x60; with smartAccountId attached will be accepted | [optional] 

## Example

```python
from pluggy_sdk.models.create_payment_intent import CreatePaymentIntent

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentIntent from a JSON string
create_payment_intent_instance = CreatePaymentIntent.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentIntent.to_json())

# convert the object into a dict
create_payment_intent_dict = create_payment_intent_instance.to_dict()
# create an instance of CreatePaymentIntent from a dict
create_payment_intent_from_dict = CreatePaymentIntent.from_dict(create_payment_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


