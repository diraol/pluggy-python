# PaymentIntentParameter

Credentials neccesary to create a payment intent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpf** | **str** | CPF of the payer | 
**cnpj** | **str** | CNPJ of the payer | [optional] 
**name** | **str** | Name of the payer. Only required for automatic pix payment requests. | [optional] 

## Example

```python
from pluggy_sdk.models.payment_intent_parameter import PaymentIntentParameter

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentParameter from a JSON string
payment_intent_parameter_instance = PaymentIntentParameter.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentParameter.to_json())

# convert the object into a dict
payment_intent_parameter_dict = payment_intent_parameter_instance.to_dict()
# create an instance of PaymentIntentParameter from a dict
payment_intent_parameter_from_dict = PaymentIntentParameter.from_dict(payment_intent_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


