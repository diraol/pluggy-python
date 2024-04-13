# PaymentRecipientAccount

Payment receiver bank account information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | Receiver bank account branch (agency) | 
**number** | **str** | Receiver bank account number | 
**type** | **str** | Receiver bank account type | 

## Example

```python
from pluggy_sdk.models.payment_recipient_account import PaymentRecipientAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRecipientAccount from a JSON string
payment_recipient_account_instance = PaymentRecipientAccount.from_json(json)
# print the JSON string representation of the object
print(PaymentRecipientAccount.to_json())

# convert the object into a dict
payment_recipient_account_dict = payment_recipient_account_instance.to_dict()
# create an instance of PaymentRecipientAccount from a dict
payment_recipient_account_from_dict = PaymentRecipientAccount.from_dict(payment_recipient_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


