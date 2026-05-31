# IdentityResponseFinancialRelationshipsProcuratorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of relationship with the client. Legal representative — natural person who represents the entity and is named in its incorporation document. Procurator — any person authorized in writing to represent the client in some business | 
**cpf_number** | **str** | CPF of the procurator. For business links this field may hold a CPF or a CNPJ (kept for backward compatibility — prefer documentNumber + documentType) | 
**document_number** | **str** | Document number of the procurator (CPF or CNPJ). Mirrors cpfNumber and is the canonical value to read | [optional] 
**document_type** | **str** | Type of document carried by documentNumber | [optional] 
**civil_name** | **str** | Civil name of the procurator. For business procurators, may hold the company name | 
**social_name** | **str** | Social name of the procurator, if any | [optional] 

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


