# PaymentIntent

Request with information related to a payment intent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | [optional] 
**status** | **str** | Payment intent status | [optional] 
**created_at** | **datetime** | Date when the payment intent was created | [optional] 
**updated_at** | **datetime** | Date when the payment intent was updated | [optional] 
**payment_request** | [**PaymentRequest**](PaymentRequest.md) | Payment request associated to the payment intent | [optional] 
**connector** | [**Connector**](Connector.md) | Connector associated to the payment intent | [optional] 
**consent_url** | **str** | Url to authorize the payment intent | [optional] 
**reference_id** | **str** | Pix id related to the payment intent | [optional] 
**payment_method** | **str** | Payment method can be PIS (Payment Initiation) or PIX | [optional] [default to 'PIS']
**pix_data** | [**PixData**](PixData.md) | Pix data related to the payment intent (only applies for PIX payment method) | [optional] 
**error_detail** | [**PaymentIntentErrorDetail**](PaymentIntentErrorDetail.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.payment_intent import PaymentIntent

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntent from a JSON string
payment_intent_instance = PaymentIntent.from_json(json)
# print the JSON string representation of the object
print(PaymentIntent.to_json())

# convert the object into a dict
payment_intent_dict = payment_intent_instance.to_dict()
# create an instance of PaymentIntent from a dict
payment_intent_from_dict = PaymentIntent.from_dict(payment_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


