# CreateSmartTransferPayment

Create smart transfer payment request data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preauthorization_id** | **str** | Primary identifier of the preauthorization | 
**recipient_id** | **str** | Primary identifier of the paymen recipient | 
**amount** | **float** | Payment amount | 
**description** | **str** | Payment description | [optional] 
**client_payment_id** | **str** | Client payment identifier | [optional] 

## Example

```python
from pluggy_sdk.models.create_smart_transfer_payment import CreateSmartTransferPayment

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSmartTransferPayment from a JSON string
create_smart_transfer_payment_instance = CreateSmartTransferPayment.from_json(json)
# print the JSON string representation of the object
print(CreateSmartTransferPayment.to_json())

# convert the object into a dict
create_smart_transfer_payment_dict = create_smart_transfer_payment_instance.to_dict()
# create an instance of CreateSmartTransferPayment from a dict
create_smart_transfer_payment_from_dict = CreateSmartTransferPayment.from_dict(create_smart_transfer_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


