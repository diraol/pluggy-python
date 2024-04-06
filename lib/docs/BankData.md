# BankData

Bank account additional fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_number** | **str** | Complete number of the bank account &#x60;(agency code / account number)&#x60; | [optional] 
**closing_balance** | **float** | Balance including not posted transactions | [optional] 
**automatically_invested_balance** | **float** | Balance automatically invested in the account by the FI | [optional] 

## Example

```python
from pluggy_sdk.models.bank_data import BankData

# TODO update the JSON string below
json = "{}"
# create an instance of BankData from a JSON string
bank_data_instance = BankData.from_json(json)
# print the JSON string representation of the object
print(BankData.to_json())

# convert the object into a dict
bank_data_dict = bank_data_instance.to_dict()
# create an instance of BankData from a dict
bank_data_form_dict = bank_data.from_dict(bank_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


