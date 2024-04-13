# LoanPaymentReleaseOverParcel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fees** | [**List[LoanPaymentReleaseOverParcelFee]**](LoanPaymentReleaseOverParcelFee.md) | List of fees that were paid outside the installment, only for single payment | [optional] 
**charges** | [**List[LoanPaymentReleaseOverParcelCharge]**](LoanPaymentReleaseOverParcelCharge.md) | List of charges that were paid out of installment | [optional] 

## Example

```python
from pluggy_sdk.models.loan_payment_release_over_parcel import LoanPaymentReleaseOverParcel

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPaymentReleaseOverParcel from a JSON string
loan_payment_release_over_parcel_instance = LoanPaymentReleaseOverParcel.from_json(json)
# print the JSON string representation of the object
print(LoanPaymentReleaseOverParcel.to_json())

# convert the object into a dict
loan_payment_release_over_parcel_dict = loan_payment_release_over_parcel_instance.to_dict()
# create an instance of LoanPaymentReleaseOverParcel from a dict
loan_payment_release_over_parcel_from_dict = LoanPaymentReleaseOverParcel.from_dict(loan_payment_release_over_parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


