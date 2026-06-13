# PaymentRequestRecipient

Recipient embedded inside a payment request. Polymorphic depending on the kind of payment. - `BANK_ACCOUNT`: a registered bank-account recipient (see `PaymentRecipient`). - `PIX_QR_CODE`: recipient derived from a PIX QR code attached to the request. - `BOLETO`: recipient derived from a boleto attached to the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Recipient discriminator. Always &#x60;BANK_ACCOUNT&#x60; for this schema. | 
**id** | **str** | Primary identifier | 
**tax_number** | **str** | Recipient CPF or CNPJ from the boleto | 
**name** | **str** | Recipient name from the boleto | 
**payment_institution** | [**PaymentInstitution**](PaymentInstitution.md) | Institution that holds the recipient&#39;s bank account. | 
**is_default** | **bool** | Indicates if the recipient is the default one | 
**account** | [**PaymentRecipientAccount**](PaymentRecipientAccount.md) |  | 
**pix_key** | **str** | Pix key associated with the payment recipient | [optional] 
**created_at** | **datetime** | Date when the payment recipient was created | 
**updated_at** | **datetime** | Date when the payment recipient was last updated | 

## Example

```python
from pluggy_sdk.models.payment_request_recipient import PaymentRequestRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestRecipient from a JSON string
payment_request_recipient_instance = PaymentRequestRecipient.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestRecipient.to_json())

# convert the object into a dict
payment_request_recipient_dict = payment_request_recipient_instance.to_dict()
# create an instance of PaymentRequestRecipient from a dict
payment_request_recipient_from_dict = PaymentRequestRecipient.from_dict(payment_request_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


