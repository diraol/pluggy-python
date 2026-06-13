# Account

Account of type bank

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary account identifier | 
**type** | **str** | Top-level account category. - &#x60;BANK&#x60;: deposit accounts (checking, savings). The &#x60;bankData&#x60; object is populated. - &#x60;CREDIT&#x60;: credit-card accounts. The &#x60;creditData&#x60; object is populated. | 
**subtype** | **str** | Account subtype within its &#x60;type&#x60;. - &#x60;CHECKING_ACCOUNT&#x60;: conta corrente (&#x60;type&#x3D;BANK&#x60;). - &#x60;SAVINGS_ACCOUNT&#x60;: conta poupança (&#x60;type&#x3D;BANK&#x60;). - &#x60;CREDIT_CARD&#x60;: credit card account (&#x60;type&#x3D;CREDIT&#x60;). For these the &#x60;number&#x60; field is masked to the last 4 digits. | 
**number** | **str** | External identifier of the account | 
**name** | **str** | Name of the account in a descriptive format | 
**marketing_name** | **str** | Name of the account as defined externally | [optional] 
**balance** | **float** | Funds of the account | 
**item_id** | **UUID** | Attached item&#39;s primary identifier | 
**tax_number** | **str** | Tax ID of the corresponding owner | [optional] 
**owner** | **str** | Name of the owner of the account | [optional] 
**currency_code** | **str** | Code referencing the currency of the balance | 
**bank_data** | [**BankData**](BankData.md) |  | [optional] 
**credit_data** | [**CreditData**](CreditData.md) |  | [optional] 
**created_at** | **datetime** | Date when the account was first created in Pluggy | 
**updated_at** | **datetime** | Date of the last update of the account data | 

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
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


