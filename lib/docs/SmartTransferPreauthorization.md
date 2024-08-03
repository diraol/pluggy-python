# SmartTransferPreauthorization

Smart transfer preauthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Preauthorization primary identifier | 
**status** | **str** | Preauthorization status | 
**consent_url** | **str** | Url to give the consent in the institution | [optional] 
**client_preauthorization_id** | **str** | Client preauthorization identifier | [optional] 
**callback_urls** | [**SmartTransferCallbackUrls**](SmartTransferCallbackUrls.md) |  | [optional] 
**recipients** | [**List[PaymentRecipient]**](PaymentRecipient.md) |  | 
**connector** | [**Connector**](Connector.md) |  | 
**created_at** | **datetime** | Date when the preauthorization was created | 
**updated_at** | **datetime** | Date when the preauthorization was updated | 

## Example

```python
from pluggy_sdk.models.smart_transfer_preauthorization import SmartTransferPreauthorization

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPreauthorization from a JSON string
smart_transfer_preauthorization_instance = SmartTransferPreauthorization.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPreauthorization.to_json())

# convert the object into a dict
smart_transfer_preauthorization_dict = smart_transfer_preauthorization_instance.to_dict()
# create an instance of SmartTransferPreauthorization from a dict
smart_transfer_preauthorization_from_dict = SmartTransferPreauthorization.from_dict(smart_transfer_preauthorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


