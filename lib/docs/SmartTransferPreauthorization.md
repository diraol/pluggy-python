# SmartTransferPreauthorization

Smart transfer preauthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Preauthorization primary identifier | 
**status** | **str** | Preauthorization lifecycle status. - &#x60;CREATED&#x60;: the preauthorization was created and is awaiting the payer&#39;s consent (see &#x60;consentUrl&#x60;). - &#x60;COMPLETED&#x60;: the payer authorized the consent. The preauthorization can now be used to execute payments. - &#x60;REJECTED&#x60;: the payer rejected the consent. - &#x60;REVOKED&#x60;: the consent was revoked after being authorized. - &#x60;ERROR&#x60;: the preauthorization flow failed unexpectedly (see &#x60;errorDetail&#x60;). | 
**consent_url** | **str** | Url to give the consent in the institution | [optional] 
**client_preauthorization_id** | **str** | Client preauthorization identifier | [optional] 
**callback_urls** | [**SmartTransferCallbackUrls**](SmartTransferCallbackUrls.md) |  | [optional] 
**recipients** | [**List[PaymentRecipient]**](PaymentRecipient.md) |  | 
**connector** | [**Connector**](Connector.md) |  | 
**created_at** | **datetime** | Date when the preauthorization was created | 
**updated_at** | **datetime** | Date when the preauthorization was updated | 
**configuration** | [**SmartTransferPreauthorizationConfiguration**](SmartTransferPreauthorizationConfiguration.md) |  | [optional] 
**error_detail** | [**SmartTransferPreauthorizationErrorDetail**](SmartTransferPreauthorizationErrorDetail.md) |  | [optional] 

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


