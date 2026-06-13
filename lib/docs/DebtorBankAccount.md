# DebtorBankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency** | **str** | Branch number | [optional] 
**account** | **str** | Account number | [optional] 
**name** | **str** | Bank name | [optional] 

## Example

```python
from pluggy_sdk.models.debtor_bank_account import DebtorBankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of DebtorBankAccount from a JSON string
debtor_bank_account_instance = DebtorBankAccount.from_json(json)
# print the JSON string representation of the object
print(DebtorBankAccount.to_json())

# convert the object into a dict
debtor_bank_account_dict = debtor_bank_account_instance.to_dict()
# create an instance of DebtorBankAccount from a dict
debtor_bank_account_from_dict = DebtorBankAccount.from_dict(debtor_bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


