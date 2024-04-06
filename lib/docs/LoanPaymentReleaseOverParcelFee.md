# LoanPaymentReleaseOverParcelFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Denomination of the agreed rate | [optional] 
**code** | **str** | Acronym identifying the agreed rate | [optional] 
**amount** | **float** | Monetary value of the tariff agreed in the contract | [optional] 

## Example

```python
from pluggy_sdk.models.loan_payment_release_over_parcel_fee import LoanPaymentReleaseOverParcelFee

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPaymentReleaseOverParcelFee from a JSON string
loan_payment_release_over_parcel_fee_instance = LoanPaymentReleaseOverParcelFee.from_json(json)
# print the JSON string representation of the object
print(LoanPaymentReleaseOverParcelFee.to_json())

# convert the object into a dict
loan_payment_release_over_parcel_fee_dict = loan_payment_release_over_parcel_fee_instance.to_dict()
# create an instance of LoanPaymentReleaseOverParcelFee from a dict
loan_payment_release_over_parcel_fee_form_dict = loan_payment_release_over_parcel_fee.from_dict(loan_payment_release_over_parcel_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


