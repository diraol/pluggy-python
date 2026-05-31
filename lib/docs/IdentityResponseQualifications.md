# IdentityResponseQualifications

Information that allows understanding since when the consulted person has been a client of the institution, as well as an indicator of the products and services they currently consume and their representatives

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_cnpj** | **str** | CNPJ of the company | 
**occupation_code** | **str** | Occupation code | [optional] 
**occupation_description** | **str** | Free-text occupation description. When occupationCode is RECEITA_FEDERAL or CBO it holds the standardized list code; when OUTRO it describes the occupation in cases where the institution does not follow the Receita Federal nor the CBO list | [optional] 
**informed_income** | [**IdentityResponseQualificationsInformedIncome**](IdentityResponseQualificationsInformedIncome.md) |  | [optional] 
**informed_patrimony** | [**IdentityResponseQualificationsInformedPatrimony**](IdentityResponseQualificationsInformedPatrimony.md) |  | [optional] 
**economic_activities** | [**List[EconomicActivity]**](EconomicActivity.md) | List of CNAE codes describing the economic activities of the business (Brazilian National Classification of Economic Activities). Only one entry per response should be marked as main | [optional] 
**informed_revenue** | [**InformedRevenue**](InformedRevenue.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.identity_response_qualifications import IdentityResponseQualifications

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityResponseQualifications from a JSON string
identity_response_qualifications_instance = IdentityResponseQualifications.from_json(json)
# print the JSON string representation of the object
print(IdentityResponseQualifications.to_json())

# convert the object into a dict
identity_response_qualifications_dict = identity_response_qualifications_instance.to_dict()
# create an instance of IdentityResponseQualifications from a dict
identity_response_qualifications_from_dict = IdentityResponseQualifications.from_dict(identity_response_qualifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


