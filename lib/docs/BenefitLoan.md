# BenefitLoan

Information related to a benefit loan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_code** | **str** | Contract code given by the contracting institution | [optional] 
**hiscon_contract_code** | **str** | Contract code given in the hiscon file | 
**cnpj_original_contract_creditor** | **str** | CNPJ of the original creditor of the contract | [optional] 
**effective_interest_rate** | **float** | Effective interest rate | [optional] 
**cet_annual_rate** | **float** | CET annual rate | [optional] 
**cet_month_rate** | **float** | CET monthly rate | [optional] 
**currency_code** | **str** | Code referencing the currency of the loan | [optional] 
**amortization_regime** | **str** | Amortization regime | [optional] 
**installments_quantity** | **float** | Number of installments | [optional] 
**installments_value** | **float** | Installment value | [optional] 
**due_date_first_installment** | **datetime** | Due date of the first installment | [optional] 
**due_date_last_installment** | **datetime** | Due date of the last installment | [optional] 
**cnpj_correspondent_banking** | **str** | CNPJ of the correspondent banking | [optional] 
**operation_hiring_date** | **datetime** | Operation hiring date | [optional] 
**client** | [**BenefitLoanClient**](BenefitLoanClient.md) |  | 

## Example

```python
from pluggy_sdk.models.benefit_loan import BenefitLoan

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitLoan from a JSON string
benefit_loan_instance = BenefitLoan.from_json(json)
# print the JSON string representation of the object
print(BenefitLoan.to_json())

# convert the object into a dict
benefit_loan_dict = benefit_loan_instance.to_dict()
# create an instance of BenefitLoan from a dict
benefit_loan_from_dict = BenefitLoan.from_dict(benefit_loan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


