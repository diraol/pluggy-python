# PaymentReceiptPerson

Debtor or creditor information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Person name | [optional] 
**tax_number** | **str** | Person tax number | [optional] 
**bank_account** | [**PaymentReceiptBankAccount**](PaymentReceiptBankAccount.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.payment_receipt_person import PaymentReceiptPerson

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReceiptPerson from a JSON string
payment_receipt_person_instance = PaymentReceiptPerson.from_json(json)
# print the JSON string representation of the object
print(PaymentReceiptPerson.to_json())

# convert the object into a dict
payment_receipt_person_dict = payment_receipt_person_instance.to_dict()
# create an instance of PaymentReceiptPerson from a dict
payment_receipt_person_from_dict = PaymentReceiptPerson.from_dict(payment_receipt_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


