# Account

Account of type bank

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary account identifier | 
**type** | **str** | Type of account, may be BANK or CREDIT | 
**subtype** | **str** | Subtype of corresponding type of account | 
**number** | **str** | External identifier of the account | 
**name** | **str** | Name of the account in a descriptive format | 
**marketing_name** | **str** | Name of the account as defined externally | [optional] 
**balance** | **float** | Funds of the account | 
**item_id** | **str** | Attached item&#39;s primary identifier | 
**tax_number** | **str** | Tax ID of the corresponding owner | [optional] 
**owner** | **str** | Name of the owner of the account | [optional] 
**currency_code** | **str** | Code referencing the currency of the balance | 
**bank_data** | [**BankData**](BankData.md) |  | [optional] 
**credit_data** | [**CreditData**](CreditData.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_form_dict = account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


