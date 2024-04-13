# LoanInstallmentBalloonPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **datetime** | Expiration date of the non-regular installment to expire from the contract of the consulted credit modality | [optional] 
**amount** | [**LoanInstallmentBalloonPaymentAmount**](LoanInstallmentBalloonPaymentAmount.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.loan_installment_balloon_payment import LoanInstallmentBalloonPayment

# TODO update the JSON string below
json = "{}"
# create an instance of LoanInstallmentBalloonPayment from a JSON string
loan_installment_balloon_payment_instance = LoanInstallmentBalloonPayment.from_json(json)
# print the JSON string representation of the object
print(LoanInstallmentBalloonPayment.to_json())

# convert the object into a dict
loan_installment_balloon_payment_dict = loan_installment_balloon_payment_instance.to_dict()
# create an instance of LoanInstallmentBalloonPayment from a dict
loan_installment_balloon_payment_from_dict = LoanInstallmentBalloonPayment.from_dict(loan_installment_balloon_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


