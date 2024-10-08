# IdentityResponse

Response with details personal information related to the owner of the connection's account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the identity to retrieve | 
**item_id** | **str** | Identifier of the item linked to the identity | 
**birth_date** | **datetime** | Date of birth | [optional] 
**tax_number** | **str** | The tax ID (CNPJ) associated with the business account | [optional] 
**document** | **str** | Primary document that identifies the owner | [optional] 
**document_type** | **str** | Type of document collected | [optional] 
**job_title** | **str** | Profession or Job information | [optional] 
**full_name** | **str** | Name of the owner of the account | [optional] 
**establishment_code** | **str** | Establishment code (only for PAYMENT_ACCOUNT connectors) | [optional] 
**establishment_name** | **str** | Name of the establishment (only for PAYMENT_ACCOUNT connectors) | [optional] 
**company_name** | **str** | For business connector, the name of the business | [optional] 
**phone_numbers** | [**List[PhoneNumber]**](PhoneNumber.md) | List of phone numbers related to the account | [optional] 
**emails** | [**List[Email]**](Email.md) | List of email addresses related to the account | [optional] 
**addresses** | [**List[Address]**](Address.md) | List of addresses related to the account | [optional] 
**relations** | [**List[IdentityRelation]**](IdentityRelation.md) | List of names related to the account | [optional] 
**investor_profile** | **str** | Is a rating that indicates the investor personality and motivation for investing | [optional] 
**qualifications** | [**IdentityResponseQualifications**](IdentityResponseQualifications.md) |  | [optional] 
**financial_relationships** | [**IdentityResponseFinancialRelationships**](IdentityResponseFinancialRelationships.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.identity_response import IdentityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityResponse from a JSON string
identity_response_instance = IdentityResponse.from_json(json)
# print the JSON string representation of the object
print(IdentityResponse.to_json())

# convert the object into a dict
identity_response_dict = identity_response_instance.to_dict()
# create an instance of IdentityResponse from a dict
identity_response_from_dict = IdentityResponse.from_dict(identity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


