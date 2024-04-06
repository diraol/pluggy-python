# LoanPayments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_outstanding_balance** | **float** | Amount required for the customer to settle the debt | [optional] 
**releases** | [**List[LoanPaymentRelease]**](LoanPaymentRelease.md) | List of payments made in the period | [optional] 

## Example

```python
from pluggy_sdk.models.loan_payments import LoanPayments

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPayments from a JSON string
loan_payments_instance = LoanPayments.from_json(json)
# print the JSON string representation of the object
print(LoanPayments.to_json())

# convert the object into a dict
loan_payments_dict = loan_payments_instance.to_dict()
# create an instance of LoanPayments from a dict
loan_payments_form_dict = loan_payments.from_dict(loan_payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


