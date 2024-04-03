# UpdatePaymentRecipient

Request with information to update a payment recipient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** | Account owner tax number. Can be CPF or CNPJ (only numbers) | [optional] 
**name** | **str** | Account owner name | [optional] 
**payment_institution_id** | **str** | Primary identifier of the institution associated to the payment recipient | [optional] 
**account** | [**PaymentRecipientAccount**](PaymentRecipientAccount.md) |  | [optional] 
**is_default** | **bool** | Indicates if the recipient is the default one | [optional] 

## Example

```python
from openapi_client.models.update_payment_recipient import UpdatePaymentRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentRecipient from a JSON string
update_payment_recipient_instance = UpdatePaymentRecipient.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentRecipient.to_json())

# convert the object into a dict
update_payment_recipient_dict = update_payment_recipient_instance.to_dict()
# create an instance of UpdatePaymentRecipient from a dict
update_payment_recipient_form_dict = update_payment_recipient.from_dict(update_payment_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


