# CreatePaymentIntent

Request with information to create a payment intent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_request_id** | **str** | Primary identifier of the payment request associated to the payment intent | [optional] 
**parameters** | [**PaymentIntentParameter**](PaymentIntentParameter.md) |  | [optional] 
**connector_id** | **float** | Primary identifier of the connector associated to the payment intent | [optional] 
**payment_method** | **str** | Payment method can be PIS (Payment Initiation) or PIX (PIX QR flow). | [optional] 
**is_dynamic_pix** | **bool** | Only for PIX paymentMethod. If true, the generated PIX QR code is dynamic and one-use. This requires the customerId to be present, and the customer must have CPF/CNPJ | [optional] 

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


