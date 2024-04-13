# LoanContractedFinanceCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Charge type agreed in the contract (https://openbanking-brasil.github.io/openapi/swagger-apis/loans/?urls.primaryName&#x3D;2.0.1#model-EnumContractFinanceChargeType) | [optional] 
**additional_info** | **str** | Field for additional information | [optional] 
**rate** | **float** | Charge value in percentage agreed in the contract | [optional] 

## Example

```python
from pluggy_sdk.models.loan_contracted_finance_charge import LoanContractedFinanceCharge

# TODO update the JSON string below
json = "{}"
# create an instance of LoanContractedFinanceCharge from a JSON string
loan_contracted_finance_charge_instance = LoanContractedFinanceCharge.from_json(json)
# print the JSON string representation of the object
print(LoanContractedFinanceCharge.to_json())

# convert the object into a dict
loan_contracted_finance_charge_dict = loan_contracted_finance_charge_instance.to_dict()
# create an instance of LoanContractedFinanceCharge from a dict
loan_contracted_finance_charge_from_dict = LoanContractedFinanceCharge.from_dict(loan_contracted_finance_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


