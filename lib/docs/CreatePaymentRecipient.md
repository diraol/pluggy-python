# CreatePaymentRecipient

Request with information to create a payment recipient, there is two form to create a payment recipient, one with pixKey and other with taxNumber, name, paymentInstitutionId and account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** | Account owner tax number. Can be CPF or CNPJ (only numbers). Send only when the pixKey is not sent. | [optional] 
**name** | **str** | Account owner name. Send only this when the pixKey is not sent. | [optional] 
**payment_institution_id** | **str** | Primary identifier of the institution associated to the payment recipient. Send only when the pixKey is not sent. | [optional] 
**account** | [**PaymentRecipientAccount**](PaymentRecipientAccount.md) | Recipient&#39;s bank account destination. Send only if the pixKey is not sent. | [optional] 
**is_default** | **bool** | Indicates if the recipient is the default one | [optional] 
**pix_key** | **str** | Pix key associated with the payment recipient | [optional] 

## Example

```python
from pluggy_sdk.models.create_payment_recipient import CreatePaymentRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentRecipient from a JSON string
create_payment_recipient_instance = CreatePaymentRecipient.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentRecipient.to_json())

# convert the object into a dict
create_payment_recipient_dict = create_payment_recipient_instance.to_dict()
# create an instance of CreatePaymentRecipient from a dict
create_payment_recipient_from_dict = CreatePaymentRecipient.from_dict(create_payment_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


