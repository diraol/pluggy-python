# PayrollLoan

Information related to a payroll loan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_code** | **str** | Contract code given by the contracting institution | 
**cnpj_original_contract_creditor** | **str** | CNPJ of the original creditor of the contract | [optional] 
**nominal_interest_rate** | **float** | Nominal interest rate | [optional] 
**efective_interest_rate** | **float** | Effective interest rate | [optional] 
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
**client** | [**PayrollLoanClient**](PayrollLoanClient.md) |  | 

## Example

```python
from pluggy_sdk.models.payroll_loan import PayrollLoan

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollLoan from a JSON string
payroll_loan_instance = PayrollLoan.from_json(json)
# print the JSON string representation of the object
print(PayrollLoan.to_json())

# convert the object into a dict
payroll_loan_dict = payroll_loan_instance.to_dict()
# create an instance of PayrollLoan from a dict
payroll_loan_from_dict = PayrollLoan.from_dict(payroll_loan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


