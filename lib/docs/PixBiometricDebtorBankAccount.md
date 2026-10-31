# PixBiometricDebtorBankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency** | **str** | Branch number | 
**account** | **str** | Account number, masked | 
**name** | **str** | Institution name | 

## Example

```python
from pluggy_sdk.models.pix_biometric_debtor_bank_account import PixBiometricDebtorBankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricDebtorBankAccount from a JSON string
pix_biometric_debtor_bank_account_instance = PixBiometricDebtorBankAccount.from_json(json)
# print the JSON string representation of the object
print(PixBiometricDebtorBankAccount.to_json())

# convert the object into a dict
pix_biometric_debtor_bank_account_dict = pix_biometric_debtor_bank_account_instance.to_dict()
# create an instance of PixBiometricDebtorBankAccount from a dict
pix_biometric_debtor_bank_account_from_dict = PixBiometricDebtorBankAccount.from_dict(pix_biometric_debtor_bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


