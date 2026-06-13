# SmartAccount

Pluggy Smart Account (escrow account) attached to a payment request. Receives funds and lets the client orchestrate splits and withdrawals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**agency** | **str** | Bank agency of the smart account | 
**number** | **str** | Account number | 
**verifying_digit** | **str** | Account verifying digit | 
**type** | **str** | Smart accounts are always checking accounts | 
**is_sandbox** | **bool** |  | 
**owner** | **str** | Legal name of the smart account holder. Only returned in detailed views. | [optional] 
**pix_key** | **str** | PIX key associated with the smart account | [optional] 

## Example

```python
from pluggy_sdk.models.smart_account import SmartAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SmartAccount from a JSON string
smart_account_instance = SmartAccount.from_json(json)
# print the JSON string representation of the object
print(SmartAccount.to_json())

# convert the object into a dict
smart_account_dict = smart_account_instance.to_dict()
# create an instance of SmartAccount from a dict
smart_account_from_dict = SmartAccount.from_dict(smart_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


