# CreateSmartAccountRequest

Create smart account request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Account owner fullName | 
**tax_number** | **str** | Account owner tax number (CPF or CNPJ) | 
**email** | **str** | Account owner email | 
**phone_number** | **str** | Account owner phone | 
**is_sandbox** | **bool** | Indicates if the smart account is a sandbox account | [optional] 
**address** | [**SmartAccountAddress**](SmartAccountAddress.md) |  | 

## Example

```python
from pluggy_sdk.models.create_smart_account_request import CreateSmartAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSmartAccountRequest from a JSON string
create_smart_account_request_instance = CreateSmartAccountRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSmartAccountRequest.to_json())

# convert the object into a dict
create_smart_account_request_dict = create_smart_account_request_instance.to_dict()
# create an instance of CreateSmartAccountRequest from a dict
create_smart_account_request_from_dict = CreateSmartAccountRequest.from_dict(create_smart_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


