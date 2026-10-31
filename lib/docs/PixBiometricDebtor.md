# PixBiometricDebtor

The linked account, as the institution reported it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Account holder name | 
**tax_number** | **str** | Account holder CPF/CNPJ, masked | 
**bank_account** | [**PixBiometricDebtorBankAccount**](PixBiometricDebtorBankAccount.md) |  | 

## Example

```python
from pluggy_sdk.models.pix_biometric_debtor import PixBiometricDebtor

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricDebtor from a JSON string
pix_biometric_debtor_instance = PixBiometricDebtor.from_json(json)
# print the JSON string representation of the object
print(PixBiometricDebtor.to_json())

# convert the object into a dict
pix_biometric_debtor_dict = pix_biometric_debtor_instance.to_dict()
# create an instance of PixBiometricDebtor from a dict
pix_biometric_debtor_from_dict = PixBiometricDebtor.from_dict(pix_biometric_debtor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


