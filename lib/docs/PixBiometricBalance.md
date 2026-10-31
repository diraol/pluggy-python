# PixBiometricBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Account balance in BRL. | 
**overdraft** | [**SmartTransferOverdraft**](SmartTransferOverdraft.md) | Overdraft limit of the account. Null when the institution does not share it. | 

## Example

```python
from pluggy_sdk.models.pix_biometric_balance import PixBiometricBalance

# TODO update the JSON string below
json = "{}"
# create an instance of PixBiometricBalance from a JSON string
pix_biometric_balance_instance = PixBiometricBalance.from_json(json)
# print the JSON string representation of the object
print(PixBiometricBalance.to_json())

# convert the object into a dict
pix_biometric_balance_dict = pix_biometric_balance_instance.to_dict()
# create an instance of PixBiometricBalance from a dict
pix_biometric_balance_from_dict = PixBiometricBalance.from_dict(pix_biometric_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


