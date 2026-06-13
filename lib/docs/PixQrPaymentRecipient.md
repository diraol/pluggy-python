# PixQrPaymentRecipient

Payment recipient inferred from a PIX QR code (only the merchant name is exposed).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Merchant name decoded from the PIX QR code | [optional] 

## Example

```python
from pluggy_sdk.models.pix_qr_payment_recipient import PixQrPaymentRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of PixQrPaymentRecipient from a JSON string
pix_qr_payment_recipient_instance = PixQrPaymentRecipient.from_json(json)
# print the JSON string representation of the object
print(PixQrPaymentRecipient.to_json())

# convert the object into a dict
pix_qr_payment_recipient_dict = pix_qr_payment_recipient_instance.to_dict()
# create an instance of PixQrPaymentRecipient from a dict
pix_qr_payment_recipient_from_dict = PixQrPaymentRecipient.from_dict(pix_qr_payment_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


