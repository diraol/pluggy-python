# PaymentRecipient

Response with information related to a payment recipient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**tax_number** | **str** | Account owner tax number. Can be CPF or CNPJ (only numbers) | 
**name** | **str** | Account owner name | 
**payment_institution** | [**PaymentInstitution**](PaymentInstitution.md) |  | [optional] 
**is_default** | **bool** | Indicates if the recipient is the default one | [optional] 
**account** | [**PaymentRecipientAccount**](PaymentRecipientAccount.md) |  | 

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


