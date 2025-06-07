# PaymentIntentAutomaticPix

Automatic PIX data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_amount** | **float** | Fixed charge amount; if filled in, it represents consent for payments of fixed amounts, not subject to change during the validity of the consent. If it&#39;s sent, minimumVariableAmount and maximumVariableAmount cannot be provided. | [optional] 
**minimum_variable_amount** | **float** | Minimum amount allowed per charge; if filled in, it represents consent for payments of variable amounts. If it&#39;s sent, fixedAmount cannot be provided. | [optional] 
**maximum_variable_amount** | **float** | Maximum amount allowed per charge; if filled in, it represents consent for payments of variable amounts. If it&#39;s sent, fixedAmount cannot be provided. | [optional] 
**start_date** | **datetime** | Represents the expected date for the first occurrence of a payment associated with the recurrence. | 
**expires_at** | **datetime** | Expiration date for the automatic pix authorization | [optional] 
**is_retry_accepted** | **bool** | Indicates whether the receiving customer is allowed to make payment attempts, according to the rules established in the Pix arrangement. | [optional] 
**first_payment** | [**AutomaticPixFirstPayment**](AutomaticPixFirstPayment.md) |  | [optional] 
**interval** | **str** | Defines the permitted frequency for carrying out transactions. | 

## Example

```python
from pluggy_sdk.models.payment_intent_automatic_pix import PaymentIntentAutomaticPix

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentAutomaticPix from a JSON string
payment_intent_automatic_pix_instance = PaymentIntentAutomaticPix.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentAutomaticPix.to_json())

# convert the object into a dict
payment_intent_automatic_pix_dict = payment_intent_automatic_pix_instance.to_dict()
# create an instance of PaymentIntentAutomaticPix from a dict
payment_intent_automatic_pix_from_dict = PaymentIntentAutomaticPix.from_dict(payment_intent_automatic_pix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


