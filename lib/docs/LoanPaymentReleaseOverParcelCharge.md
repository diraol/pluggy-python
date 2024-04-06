# LoanPaymentReleaseOverParcelCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Charge type agreed in the contract (https://openbanking-brasil.github.io/openapi/swagger-apis/loans/?urls.primaryName&#x3D;2.0.1#model-EnumContractFinanceChargeType) | [optional] 
**additional_info** | **str** | Free field to fill in additional information regarding the charge | [optional] 
**amount** | **float** | Payment amount of the charge paid outside the installment | [optional] 

## Example

```python
from pluggy_sdk.models.loan_payment_release_over_parcel_charge import LoanPaymentReleaseOverParcelCharge

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPaymentReleaseOverParcelCharge from a JSON string
loan_payment_release_over_parcel_charge_instance = LoanPaymentReleaseOverParcelCharge.from_json(json)
# print the JSON string representation of the object
print(LoanPaymentReleaseOverParcelCharge.to_json())

# convert the object into a dict
loan_payment_release_over_parcel_charge_dict = loan_payment_release_over_parcel_charge_instance.to_dict()
# create an instance of LoanPaymentReleaseOverParcelCharge from a dict
loan_payment_release_over_parcel_charge_form_dict = loan_payment_release_over_parcel_charge.from_dict(loan_payment_release_over_parcel_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


