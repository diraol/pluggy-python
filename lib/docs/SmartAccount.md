# SmartAccount

Smart account product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier of the Smart account | 
**ispb** | **str** | Smart account ISP number | 
**agency** | **str** | Smart account agency number | 
**number** | **str** | Smart account number | 
**verifying_digit** | **str** | Smart account verifying digit | 
**type** | **str** | Smart account type | 
**is_sandbox** | **bool** | Indicates if the smart account is a sandbox account | 
**pix_key** | **str** | Smart account PIX key | 

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


