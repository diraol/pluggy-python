# BillFinanceCharge

Response with information related to a credit card bill finance charge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**type** | **str** | Denomination of the charges that apply to the postpaid payment account bill | 
**amount** | **float** | Amount charged for the charge/fee | 
**currency_code** | **str** | Code referencing the currency of the charge | 
**additional_info** | **str** | Free field, mandatory to fill if &#39;OTHER&#39; type of charge is selected | [optional] 

## Example

```python
from pluggy_sdk.models.bill_finance_charge import BillFinanceCharge

# TODO update the JSON string below
json = "{}"
# create an instance of BillFinanceCharge from a JSON string
bill_finance_charge_instance = BillFinanceCharge.from_json(json)
# print the JSON string representation of the object
print(BillFinanceCharge.to_json())

# convert the object into a dict
bill_finance_charge_dict = bill_finance_charge_instance.to_dict()
# create an instance of BillFinanceCharge from a dict
bill_finance_charge_from_dict = BillFinanceCharge.from_dict(bill_finance_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


