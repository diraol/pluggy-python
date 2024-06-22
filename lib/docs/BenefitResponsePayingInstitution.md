# BenefitResponsePayingInstitution

Paying institution information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Paying institution code | [optional] 
**name** | **str** | Paying institution name | [optional] 
**agency** | **str** | Paying institution agency | [optional] 
**account** | **str** | Paying institution account | [optional] 

## Example

```python
from pluggy_sdk.models.benefit_response_paying_institution import BenefitResponsePayingInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitResponsePayingInstitution from a JSON string
benefit_response_paying_institution_instance = BenefitResponsePayingInstitution.from_json(json)
# print the JSON string representation of the object
print(BenefitResponsePayingInstitution.to_json())

# convert the object into a dict
benefit_response_paying_institution_dict = benefit_response_paying_institution_instance.to_dict()
# create an instance of BenefitResponsePayingInstitution from a dict
benefit_response_paying_institution_from_dict = BenefitResponsePayingInstitution.from_dict(benefit_response_paying_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


