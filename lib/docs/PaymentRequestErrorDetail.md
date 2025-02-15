# PaymentRequestErrorDetail

Error details when payment request fails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code | [optional] 
**provider_message** | **str** | Error message returned by the institution | [optional] 

## Example

```python
from pluggy_sdk.models.payment_request_error_detail import PaymentRequestErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestErrorDetail from a JSON string
payment_request_error_detail_instance = PaymentRequestErrorDetail.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestErrorDetail.to_json())

# convert the object into a dict
payment_request_error_detail_dict = payment_request_error_detail_instance.to_dict()
# create an instance of PaymentRequestErrorDetail from a dict
payment_request_error_detail_from_dict = PaymentRequestErrorDetail.from_dict(payment_request_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


