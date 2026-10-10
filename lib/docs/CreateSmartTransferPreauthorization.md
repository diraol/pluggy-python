# CreateSmartTransferPreauthorization

Create smart transfer preauthorization request data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **float** | Primary identifier of the connector | 
**parameters** | [**SmartTransferPreauthorizationParameter**](SmartTransferPreauthorizationParameter.md) |  | 
**recipient_ids** | **List[str]** |  | 
**callback_urls** | [**SmartTransferCallbackUrls**](SmartTransferCallbackUrls.md) |  | [optional] 
**client_preauthorization_id** | **str** | Client preauthorization identifier | [optional] 
**configuration** | [**SmartTransferPreauthorizationConfiguration**](SmartTransferPreauthorizationConfiguration.md) |  | [optional] 
**linked_journey** | **bool** | When true, the user is also asked, in the same approval at the bank, for a permission to read the source account balance. Check &#x60;dataConsent&#x60; on the preauthorization and use the balance endpoint once it is &#x60;AUTHORISED&#x60;. | [optional] [default to False]

## Example

```python
from pluggy_sdk.models.create_smart_transfer_preauthorization import CreateSmartTransferPreauthorization

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSmartTransferPreauthorization from a JSON string
create_smart_transfer_preauthorization_instance = CreateSmartTransferPreauthorization.from_json(json)
# print the JSON string representation of the object
print(CreateSmartTransferPreauthorization.to_json())

# convert the object into a dict
create_smart_transfer_preauthorization_dict = create_smart_transfer_preauthorization_instance.to_dict()
# create an instance of CreateSmartTransferPreauthorization from a dict
create_smart_transfer_preauthorization_from_dict = CreateSmartTransferPreauthorization.from_dict(create_smart_transfer_preauthorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


