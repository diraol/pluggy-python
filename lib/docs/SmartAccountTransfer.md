# SmartAccountTransfer

Transfer made with money from a smart account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier of the transfer | [optional] 
**client_id** | **str** | Primary identifier of the client associated to the transfer | [optional] 
**client_payment_id** | **str** | Primary identifier of the client payment associated to the transfer | [optional] 
**amount** | **float** | Transfer amount | [optional] 
**status** | **str** | Transfer status | [optional] 
**created_at** | **datetime** | Transfer creation date | [optional] 
**updated_at** | **datetime** | Transfer last update date | [optional] 
**smart_account** | [**SmartAccount**](SmartAccount.md) |  | [optional] 
**payment_recipient** | [**PaymentRecipient**](PaymentRecipient.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.smart_account_transfer import SmartAccountTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of SmartAccountTransfer from a JSON string
smart_account_transfer_instance = SmartAccountTransfer.from_json(json)
# print the JSON string representation of the object
print(SmartAccountTransfer.to_json())

# convert the object into a dict
smart_account_transfer_dict = smart_account_transfer_instance.to_dict()
# create an instance of SmartAccountTransfer from a dict
smart_account_transfer_from_dict = SmartAccountTransfer.from_dict(smart_account_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


