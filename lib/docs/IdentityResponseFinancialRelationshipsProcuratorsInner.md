# IdentityResponseFinancialRelationshipsProcuratorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of relationship with the client | 
**cpf_number** | **str** | CPF of the procurator | 
**civil_name** | **str** | Civil name of the procurator | 
**social_name** | **str** | Social name of the procurator | [optional] 

## Example

```python
from pluggy_sdk.models.identity_response_financial_relationships_procurators_inner import IdentityResponseFinancialRelationshipsProcuratorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityResponseFinancialRelationshipsProcuratorsInner from a JSON string
identity_response_financial_relationships_procurators_inner_instance = IdentityResponseFinancialRelationshipsProcuratorsInner.from_json(json)
# print the JSON string representation of the object
print(IdentityResponseFinancialRelationshipsProcuratorsInner.to_json())

# convert the object into a dict
identity_response_financial_relationships_procurators_inner_dict = identity_response_financial_relationships_procurators_inner_instance.to_dict()
# create an instance of IdentityResponseFinancialRelationshipsProcuratorsInner from a dict
identity_response_financial_relationships_procurators_inner_from_dict = IdentityResponseFinancialRelationshipsProcuratorsInner.from_dict(identity_response_financial_relationships_procurators_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


