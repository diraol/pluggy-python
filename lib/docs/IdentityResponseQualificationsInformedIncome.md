# IdentityResponseQualificationsInformedIncome

Informed income

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | Frequency of the informed income | 
**amount** | **float** | Amount of the informed income | 
**var_date** | **datetime** | Date when the income was informed | 

## Example

```python
from pluggy_sdk.models.identity_response_qualifications_informed_income import IdentityResponseQualificationsInformedIncome

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityResponseQualificationsInformedIncome from a JSON string
identity_response_qualifications_informed_income_instance = IdentityResponseQualificationsInformedIncome.from_json(json)
# print the JSON string representation of the object
print(IdentityResponseQualificationsInformedIncome.to_json())

# convert the object into a dict
identity_response_qualifications_informed_income_dict = identity_response_qualifications_informed_income_instance.to_dict()
# create an instance of IdentityResponseQualificationsInformedIncome from a dict
identity_response_qualifications_informed_income_from_dict = IdentityResponseQualificationsInformedIncome.from_dict(identity_response_qualifications_informed_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


