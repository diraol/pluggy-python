# LoanPaymentRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_over_parcel_payment** | **bool** | Identifies whether it is an agreed payment (false) or a one-time payment (true) | [optional] 
**installment_id** | **str** | Installment identifier, responsibility of each transmitting Institution | [optional] 
**paid_date** | **datetime** | Effective date of payment referring to the contract of the credit modality consulted | [optional] 
**currency_code** | **str** | Code referencing the currency of the payment | [optional] 
**paid_amount** | **float** | Payment amount referring to the contract of the credit modality consulted | [optional] 
**over_parcel** | [**LoanPaymentReleaseOverParcel**](LoanPaymentReleaseOverParcel.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.loan_payment_release import LoanPaymentRelease

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPaymentRelease from a JSON string
loan_payment_release_instance = LoanPaymentRelease.from_json(json)
# print the JSON string representation of the object
print(LoanPaymentRelease.to_json())

# convert the object into a dict
loan_payment_release_dict = loan_payment_release_instance.to_dict()
# create an instance of LoanPaymentRelease from a dict
loan_payment_release_from_dict = LoanPaymentRelease.from_dict(loan_payment_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


