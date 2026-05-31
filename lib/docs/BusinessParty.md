# BusinessParty

Partner or administrator of a business. Partners with less than 25% shareholding may be omitted by the institution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Role of the party in the business. Administrator — runs the day-to-day, signs documents and legally responds for the entity. Partner — holds capital but may not be involved in administrative activities | 
**person_type** | **str** | Whether the party is a natural person or a legal entity | 
**document_type** | **str** | Type of the party&#39;s identification document | 
**document_number** | **str** | Number of the identification document (digits and check digit, if any) | 
**document_country** | **str** | Issuing country of the document, alpha3 ISO-3166 | [optional] 
**document_expiration_date** | **datetime** | Expiration date of the document | [optional] 
**document_issue_date** | **datetime** | Issue date of the document | [optional] 
**document_additional_info** | **str** | Free-text complement when the document carries identification info that doesn&#39;t fit the other fields | [optional] 
**civil_name** | **str** | Civil name of the party. Required when personType is NATURAL_PERSON | [optional] 
**social_name** | **str** | Social name of the natural-person party, if any | [optional] 
**company_name** | **str** | Company name of the party. Required when personType is LEGAL_ENTITY | [optional] 
**trade_name** | **str** | Trade name of the legal-entity party, if any | [optional] 
**start_date** | **datetime** | Date the party&#39;s participation started | [optional] 
**shareholding** | **float** | Shareholding fraction between 0 and 1 (e.g. 0.51 represents 51%, 1 represents 100%). Required when type is PARTNER and the shareholding is 25% or higher | [optional] 

## Example

```python
from pluggy_sdk.models.business_party import BusinessParty

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessParty from a JSON string
business_party_instance = BusinessParty.from_json(json)
# print the JSON string representation of the object
print(BusinessParty.to_json())

# convert the object into a dict
business_party_dict = business_party_instance.to_dict()
# create an instance of BusinessParty from a dict
business_party_from_dict = BusinessParty.from_dict(business_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


