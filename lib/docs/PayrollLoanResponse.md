# PayrollLoanResponse

Response with information related to a payload loan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**item_id** | **str** | Identifier of the item linked to the loan | 
**contract_code** | **str** | Contract code given by the contracting institution | [optional] 
**cnpj_original_contract_creditor** | **str** | CNPJ of the original creditor of the contract | [optional] 
**nominal_interest_rate** | **float** | Nominal interest rate | [optional] 
**efective_interest_rate** | **float** | Effective interest rate | [optional] 
**cet_annual_rate** | **float** | CET annual rate | [optional] 
**cet_month_rate** | **float** | CET monthly rate | [optional] 
**currency_code** | **str** | Code referencing the currency of the loan | 
**amortization_regime** | **str** | Amortization regime | 
**installments_quantity** | **float** | Number of installments | 
**installments_value** | **float** | Installment value | 
**due_date_first_installment** | **datetime** | Due date of the first installment | 
**due_date_last_installment** | **datetime** | Due date of the last installment | 
**cnpj_correspondent_banking** | **str** | CNPJ of the correspondent banking | [optional] 
**operation_hiring_date** | **datetime** | Operation hiring date | 
**client** | [**PayrollLoanResponseClient**](PayrollLoanResponseClient.md) |  | 

## Example

```python
from pluggy_sdk.models.payroll_loan_response import PayrollLoanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollLoanResponse from a JSON string
payroll_loan_response_instance = PayrollLoanResponse.from_json(json)
# print the JSON string representation of the object
print(PayrollLoanResponse.to_json())

# convert the object into a dict
payroll_loan_response_dict = payroll_loan_response_instance.to_dict()
# create an instance of PayrollLoanResponse from a dict
payroll_loan_response_from_dict = PayrollLoanResponse.from_dict(payroll_loan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


