# IdentityResponseFinancialRelationships

Information that allows institutions to assess, evaluate, characterize, and classify the client with the purpose of understanding their risk profile and their economic-financial capacity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Date when the relationship with the institution started | 
**products_services_type** | **List[str]** | List of products and services that the client consumes | 
**products_services_type_additional_info** | **str** | Additional info about the products and services. Populated when productsServicesType includes &#39;OUTROS&#39; | [optional] 
**procurators** | [**List[IdentityResponseFinancialRelationshipsProcuratorsInner]**](IdentityResponseFinancialRelationshipsProcuratorsInner.md) | List of procurators of the client | 
**accounts** | [**List[IdentityResponseFinancialRelationshipsAccountsInner]**](IdentityResponseFinancialRelationshipsAccountsInner.md) | List of accounts of the client with valid consent. Only accounts that have explicit user consent are returned. | [optional] 
**portabilities_received** | [**List[PortabilityReceived]**](PortabilityReceived.md) | Salary portabilities received by the institution from the client&#39;s previous paycheck banks (banco-folha). PF-only field | [optional] 
**paychecks_bank_link** | [**List[PaycheckBankLink]**](PaycheckBankLink.md) | Paycheck-bank (banco-folha) links to employers, active or formerly active. PF-only field | [optional] 

## Example

```python
from pluggy_sdk.models.identity_response_financial_relationships import IdentityResponseFinancialRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityResponseFinancialRelationships from a JSON string
identity_response_financial_relationships_instance = IdentityResponseFinancialRelationships.from_json(json)
# print the JSON string representation of the object
print(IdentityResponseFinancialRelationships.to_json())

# convert the object into a dict
identity_response_financial_relationships_dict = identity_response_financial_relationships_instance.to_dict()
# create an instance of IdentityResponseFinancialRelationships from a dict
identity_response_financial_relationships_from_dict = IdentityResponseFinancialRelationships.from_dict(identity_response_financial_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


