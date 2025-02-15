# PaymentIntentErrorDetail

Error details when payment intent fails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code | [optional] 
**provider_code** | **str** | Provider error code | [optional] 
**provider_title** | **str** | Provider error title | [optional] 
**provider_detail** | **str** | Provider detailed error description | [optional] 

## Example

```python
from pluggy_sdk.models.payment_intent_error_detail import PaymentIntentErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentErrorDetail from a JSON string
payment_intent_error_detail_instance = PaymentIntentErrorDetail.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentErrorDetail.to_json())

# convert the object into a dict
payment_intent_error_detail_dict = payment_intent_error_detail_instance.to_dict()
# create an instance of PaymentIntentErrorDetail from a dict
payment_intent_error_detail_from_dict = PaymentIntentErrorDetail.from_dict(payment_intent_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


