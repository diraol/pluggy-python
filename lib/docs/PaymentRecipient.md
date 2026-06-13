# PaymentRecipient

Bank-account payment recipient. Returned by `/payments/recipients` endpoints and embedded inside payment requests when the request targets a registered recipient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Recipient discriminator. Always &#x60;BANK_ACCOUNT&#x60; for this schema. | 
**id** | **str** | Primary identifier | 
**tax_number** | **str** | Account owner tax number. Can be CPF or CNPJ (only numbers). | 
**name** | **str** | Account owner name. | 
**payment_institution** | [**PaymentInstitution**](PaymentInstitution.md) | Institution that holds the recipient&#39;s bank account. | 
**is_default** | **bool** | Indicates if the recipient is the default one | 
**account** | [**PaymentRecipientAccount**](PaymentRecipientAccount.md) |  | 
**pix_key** | **str** | Pix key associated with the payment recipient | [optional] 
**created_at** | **datetime** | Date when the payment recipient was created | 
**updated_at** | **datetime** | Date when the payment recipient was last updated | 

## Example

```python
from pluggy_sdk.models.payment_recipient import PaymentRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRecipient from a JSON string
payment_recipient_instance = PaymentRecipient.from_json(json)
# print the JSON string representation of the object
print(PaymentRecipient.to_json())

# convert the object into a dict
payment_recipient_dict = payment_recipient_instance.to_dict()
# create an instance of PaymentRecipient from a dict
payment_recipient_from_dict = PaymentRecipient.from_dict(payment_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


