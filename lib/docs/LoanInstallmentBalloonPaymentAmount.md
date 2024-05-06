# LoanInstallmentBalloonPaymentAmount

Monetary value of the non-regular installment due

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Monetary value of the non-regular installment due | [optional] 
**currency_code** | **str** | Code referencing the currency of the installment | [optional] 

## Example

```python
from pluggy_sdk.models.loan_installment_balloon_payment_amount import LoanInstallmentBalloonPaymentAmount

# TODO update the JSON string below
json = "{}"
# create an instance of LoanInstallmentBalloonPaymentAmount from a JSON string
loan_installment_balloon_payment_amount_instance = LoanInstallmentBalloonPaymentAmount.from_json(json)
# print the JSON string representation of the object
print(LoanInstallmentBalloonPaymentAmount.to_json())

# convert the object into a dict
loan_installment_balloon_payment_amount_dict = loan_installment_balloon_payment_amount_instance.to_dict()
# create an instance of LoanInstallmentBalloonPaymentAmount from a dict
loan_installment_balloon_payment_amount_from_dict = LoanInstallmentBalloonPaymentAmount.from_dict(loan_installment_balloon_payment_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


