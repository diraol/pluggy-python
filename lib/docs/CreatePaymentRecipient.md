# CreatePaymentRecipient

Request with information to create a payment recipient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** | Account owner tax number. Can be CPF or CNPJ (only numbers) | 
**name** | **str** | Account owner name | 
**payment_institution_id** | **str** | Primary identifier of the institution associated to the payment recipient | 
**account** | [**PaymentRecipientAccount**](PaymentRecipientAccount.md) |  | 
**is_default** | **bool** | Indicates if the recipient is the default one | [optional] 

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
create_payment_recipient_form_dict = create_payment_recipient.from_dict(create_payment_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


