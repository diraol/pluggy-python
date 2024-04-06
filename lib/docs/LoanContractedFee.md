# LoanContractedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Agreed rate denomination | [optional] 
**code** | **str** | Acronym identifying the agreed rate | [optional] 
**charge_type** | **str** | Charge type for the rate agreed in the contract | [optional] 
**charge** | **str** | Billing method related to the tariff agreed in the contract | [optional] 
**amount** | **float** | Monetary value of the tariff agreed in the contract | [optional] 
**rate** | **float** | Rate value in percentage agreed in the contract | [optional] 

## Example

```python
from pluggy_sdk.models.loan_contracted_fee import LoanContractedFee

# TODO update the JSON string below
json = "{}"
# create an instance of LoanContractedFee from a JSON string
loan_contracted_fee_instance = LoanContractedFee.from_json(json)
# print the JSON string representation of the object
print(LoanContractedFee.to_json())

# convert the object into a dict
loan_contracted_fee_dict = loan_contracted_fee_instance.to_dict()
# create an instance of LoanContractedFee from a dict
loan_contracted_fee_form_dict = loan_contracted_fee.from_dict(loan_contracted_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


