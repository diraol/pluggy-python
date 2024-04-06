# PaymentRequestCallbackUrls

Redirect urls after the payment was completed or ended in error status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **str** | Url to be redirected after the payment was completed | [optional] 
**pending** | **str** | Url to be redirected when the payment is pending (for example, when it has status WAITING_PAYER_AUTHORIZATION | [optional] 
**error** | **str** | Url to be redirected after the payment ended in error status | [optional] 

## Example

```python
from pluggy_sdk.models.payment_request_callback_urls import PaymentRequestCallbackUrls

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestCallbackUrls from a JSON string
payment_request_callback_urls_instance = PaymentRequestCallbackUrls.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestCallbackUrls.to_json())

# convert the object into a dict
payment_request_callback_urls_dict = payment_request_callback_urls_instance.to_dict()
# create an instance of PaymentRequestCallbackUrls from a dict
payment_request_callback_urls_form_dict = payment_request_callback_urls.from_dict(payment_request_callback_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


