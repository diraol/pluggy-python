# CreatePixQrPaymentRequest

Request with information to create a PIX QR payment request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pix_qr_code** | **str** | Pix QR code | 
**callback_urls** | [**PaymentRequestCallbackUrls**](PaymentRequestCallbackUrls.md) |  | [optional] 
**customer_id** | **str** | Customer identifier associated to the payment | [optional] 

## Example

```python
from pluggy_sdk.models.create_pix_qr_payment_request import CreatePixQrPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePixQrPaymentRequest from a JSON string
create_pix_qr_payment_request_instance = CreatePixQrPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePixQrPaymentRequest.to_json())

# convert the object into a dict
create_pix_qr_payment_request_dict = create_pix_qr_payment_request_instance.to_dict()
# create an instance of CreatePixQrPaymentRequest from a dict
create_pix_qr_payment_request_form_dict = create_pix_qr_payment_request.from_dict(create_pix_qr_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


