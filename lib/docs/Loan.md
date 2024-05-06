# Loan

Response with information related to a loan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**item_id** | **str** | Identifier of the item linked to the loan | 
**contract_number** | **str** | Contract number given by the contracting institution | [optional] 
**ipoc_code** | **str** | Standard contract number - IPOC (Identificação Padronizada da Operação de Crédito) | [optional] 
**product_name** | **str** | Denomination/Identification of the name of the credit operation disclosed to the customer | 
**type** | **str** | Loan type (https://openbanking-brasil.github.io/openapi/swagger-apis/loans/?urls.primaryName&#x3D;2.0.1#model-EnumContractProductSubTypeLoans) | [optional] 
**var_date** | **datetime** | Date when the loan data was collected | 
**contract_date** | **datetime** | Date when the loan was contracted | [optional] 
**disbursement_dates** | **List[date]** | Disbursement date of the contracted amount | [optional] 
**settlement_date** | **datetime** | Loan settlement date | [optional] 
**contract_amount** | **float** | Loan contracted value | [optional] 
**currency_code** | **str** | Code referencing the currency of the loan | 
**due_date** | **datetime** | Loan due date | [optional] 
**installment_periodicity** | **str** | Installments regular frequency | [optional] 
**installment_periodicity_additional_info** | **str** | Mandatory field to complement the information regarding the regular payment frequency when installmentPeriodicity has value &#39;OTHERS&#39; | [optional] 
**first_installment_due_date** | **datetime** | First installment due date | [optional] 
**cet** | **float** | CET - Custo Efetivo Total must be expressed as an annual percentage rate and incorporates all charges and expenses incurred in credit operations (interest rate, but also tariffs, taxes, insurance and other expenses charged) | [optional] 
**amortization_scheduled** | **str** | Amortization system (https://openbanking-brasil.github.io/openapi/swagger-apis/loans/?urls.primaryName&#x3D;2.0.1#model-EnumContractAmortizationScheduled) | [optional] 
**amortization_scheduled_additional_info** | **str** | Mandatory field to complement the information regarding the scheduled amortization when it has value &#39;OTHERS&#39; | [optional] 
**cnpj_consignee** | **str** | Consignor CNPJ | [optional] 
**interest_rates** | [**List[LoanInterestRate]**](LoanInterestRate.md) |  | [optional] 
**contracted_fees** | [**List[LoanContractedFee]**](LoanContractedFee.md) | List that brings the information of the tariffs agreed in the contract. | [optional] 
**contracted_finance_charges** | [**List[LoanContractedFinanceCharge]**](LoanContractedFinanceCharge.md) | List that brings the charges agreed in the contract | [optional] 
**warranties** | [**List[LoanWarranty]**](LoanWarranty.md) |  | [optional] 
**installments** | [**LoanInstallments**](LoanInstallments.md) |  | [optional] 
**payments** | [**LoanPayments**](LoanPayments.md) | Loan contract payment data | [optional] 

## Example

```python
from pluggy_sdk.models.loan import Loan

# TODO update the JSON string below
json = "{}"
# create an instance of Loan from a JSON string
loan_instance = Loan.from_json(json)
# print the JSON string representation of the object
print(Loan.to_json())

# convert the object into a dict
loan_dict = loan_instance.to_dict()
# create an instance of Loan from a dict
loan_from_dict = Loan.from_dict(loan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


