# Consent

Item consent information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Consent primary identifier | 
**item_id** | **str** | Primary identifier of the item associated to the consent | 
**products** | **List[str]** | Products to be collected in the connection | 
**open_finance_permissions_granted** | **List[str]** | Products consented by the user to be collected | [optional] 
**created_at** | **datetime** | Date when the consent was given | 
**expires_at** | **datetime** | Date when the consent expires. Null if the consent doesn&#39;t expire | [optional] 
**revoked_at** | **datetime** | Date when the consent was revoked | [optional] 

## Example

```python
from pluggy_sdk.models.consent import Consent

# TODO update the JSON string below
json = "{}"
# create an instance of Consent from a JSON string
consent_instance = Consent.from_json(json)
# print the JSON string representation of the object
print(Consent.to_json())

# convert the object into a dict
consent_dict = consent_instance.to_dict()
# create an instance of Consent from a dict
consent_from_dict = Consent.from_dict(consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


