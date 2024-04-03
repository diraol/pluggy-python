# CreatePaymentIntent

Request with information to create a payment intent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_request_id** | **str** | Primary identifier of the payment request associated to the payment intent | [optional] 
**bulk_payment_id** | **str** | Primary identifier of the bulk payment associated to the payment intent | [optional] 
**connector_id** | **float** | Primary identifier of the connector associated to the payment intent | 
**parameters** | **Dict[str, str]** | Key-Value credentials neccesary to create an item | 

## Example

```python
from openapi_client.models.create_payment_intent import CreatePaymentIntent

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentIntent from a JSON string
create_payment_intent_instance = CreatePaymentIntent.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentIntent.to_json())

# convert the object into a dict
create_payment_intent_dict = create_payment_intent_instance.to_dict()
# create an instance of CreatePaymentIntent from a dict
create_payment_intent_form_dict = create_payment_intent.from_dict(create_payment_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


