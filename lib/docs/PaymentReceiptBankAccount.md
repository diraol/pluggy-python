# PaymentReceiptBankAccount

Payment bank account information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency** | **str** | Bank account branch (agency) | [optional] 
**name** | **str** | Bank account number | [optional] 
**account** | **str** | Bank account number | [optional] 

## Example

```python
from pluggy_sdk.models.payment_receipt_bank_account import PaymentReceiptBankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReceiptBankAccount from a JSON string
payment_receipt_bank_account_instance = PaymentReceiptBankAccount.from_json(json)
# print the JSON string representation of the object
print(PaymentReceiptBankAccount.to_json())

# convert the object into a dict
payment_receipt_bank_account_dict = payment_receipt_bank_account_instance.to_dict()
# create an instance of PaymentReceiptBankAccount from a dict
payment_receipt_bank_account_from_dict = PaymentReceiptBankAccount.from_dict(payment_receipt_bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


