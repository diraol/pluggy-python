# LoanInstallments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_number_of_installments** | **str** | Type of total term of the contract referring to the type of credit informed | [optional] 
**total_number_of_installments** | **float** | Total term according to the type referring to the type of credit informed | [optional] 
**type_contract_remaining** | **float** | Type of remaining term of the contract referring to the type of credit informed | [optional] 
**contract_remaining_number** | **float** | Remaining term according to the type referring to the credit type informed | [optional] 
**paid_installments** | **float** | Number of paid installments | [optional] 
**due_installments** | **float** | Number of due installments | [optional] 
**past_due_installments** | **float** | Number of overdue installments | [optional] 
**balloon_payments** | [**List[LoanInstallmentBalloonPayment]**](LoanInstallmentBalloonPayment.md) | List that brings the due dates and value of the non-regular installments of the contract of the type of credit consulted | [optional] 

## Example

```python
from pluggy_sdk.models.loan_installments import LoanInstallments

# TODO update the JSON string below
json = "{}"
# create an instance of LoanInstallments from a JSON string
loan_installments_instance = LoanInstallments.from_json(json)
# print the JSON string representation of the object
print(LoanInstallments.to_json())

# convert the object into a dict
loan_installments_dict = loan_installments_instance.to_dict()
# create an instance of LoanInstallments from a dict
loan_installments_form_dict = loan_installments.from_dict(loan_installments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


