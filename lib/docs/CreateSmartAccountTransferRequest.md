# CreateSmartAccountTransferRequest

Request with information to create a smart account transfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Transfer amount | 
**recipient_id** | **str** | Primary identifier of the recipient associated to the transfer | 
**client_payment_id** | **str** | Primary identifier of the client payment associated to the transfer | [optional] 

## Example

```python
from pluggy_sdk.models.create_smart_account_transfer_request import CreateSmartAccountTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSmartAccountTransferRequest from a JSON string
create_smart_account_transfer_request_instance = CreateSmartAccountTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSmartAccountTransferRequest.to_json())

# convert the object into a dict
create_smart_account_transfer_request_dict = create_smart_account_transfer_request_instance.to_dict()
# create an instance of CreateSmartAccountTransferRequest from a dict
create_smart_account_transfer_request_from_dict = CreateSmartAccountTransferRequest.from_dict(create_smart_account_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


