# Debtor

Information about the payer's account, as returned by the institution after the payment is completed. Only populated for `PAYMENT_COMPLETED` payment intents on connectors that expose this data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Holder name | [optional] 
**tax_number** | **str** | Obfuscated CPF/CNPJ of the payer | [optional] 
**bank_account** | [**DebtorBankAccount**](DebtorBankAccount.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.debtor import Debtor

# TODO update the JSON string below
json = "{}"
# create an instance of Debtor from a JSON string
debtor_instance = Debtor.from_json(json)
# print the JSON string representation of the object
print(Debtor.to_json())

# convert the object into a dict
debtor_dict = debtor_instance.to_dict()
# create an instance of Debtor from a dict
debtor_from_dict = Debtor.from_dict(debtor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


