# SmartTransferDataConsent

Balance permission granted with the preauthorization. Its status is refreshed from the institution when the preauthorization is retrieved by id (`GET /smart-transfers/preauthorizations/{id}`); the list returns the last known status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | AWAITING_AUTHORISATION: the user has not approved yet. AUTHORISED: the balance can be read. REJECTED: the permission was rejected, revoked, cancelled or expired; it does not come back. | 
**rejection_reason** | **str** | Why the permission is REJECTED, for example CUSTOMER_MANUALLY_REJECTED, CUSTOMER_MANUALLY_REVOKED, CONSENT_EXPIRED or CONSENT_MAX_DATE_REACHED. Null otherwise. New values may appear. | 
**updated_at** | **datetime** | When Pluggy last saw the status change. | 

## Example

```python
from pluggy_sdk.models.smart_transfer_data_consent import SmartTransferDataConsent

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferDataConsent from a JSON string
smart_transfer_data_consent_instance = SmartTransferDataConsent.from_json(json)
# print the JSON string representation of the object
print(SmartTransferDataConsent.to_json())

# convert the object into a dict
smart_transfer_data_consent_dict = smart_transfer_data_consent_instance.to_dict()
# create an instance of SmartTransferDataConsent from a dict
smart_transfer_data_consent_from_dict = SmartTransferDataConsent.from_dict(smart_transfer_data_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


