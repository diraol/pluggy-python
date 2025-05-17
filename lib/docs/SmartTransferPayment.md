# SmartTransferPayment

Smart transfer payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Payment primary identifier | 
**preauthorization_id** | **str** | Payment primary identifier | 
**status** | **str** | Payment status | 
**amount** | **float** | Payment amount | 
**description** | **str** | Payment description | [optional] 
**recipient** | [**PaymentRecipient**](PaymentRecipient.md) |  | 
**client_payment_id** | **str** | Client payment identifier | [optional] 
**created_at** | **datetime** | Date when the payemnt was created | 
**updated_at** | **datetime** | Date when the payment was updated | 

## Example

```python
from pluggy_sdk.models.smart_transfer_payment import SmartTransferPayment

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPayment from a JSON string
smart_transfer_payment_instance = SmartTransferPayment.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPayment.to_json())

# convert the object into a dict
smart_transfer_payment_dict = smart_transfer_payment_instance.to_dict()
# create an instance of SmartTransferPayment from a dict
smart_transfer_payment_from_dict = SmartTransferPayment.from_dict(smart_transfer_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


