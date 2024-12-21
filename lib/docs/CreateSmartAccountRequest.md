# CreateSmartAccountRequest

Create smart account request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Primary identifier of the item wanted to associate to the account. Mandatory unless is a sandbox account | [optional] 
**is_sandbox** | **bool** | Indicates if the smart account is a sandbox account | [optional] 
**address** | [**SmartAccountAddress**](SmartAccountAddress.md) |  | 
**tax_number** | **str** | Smart account owner&#39;s CNPJ. Just needed if &#39;isSandbox&#39; is true | [optional] 
**name** | **str** | Smart account owner&#39;s business name. Just needed if &#39;isSandbox&#39; is true | [optional] 
**email** | **str** | Email to be associated to the smart account | 
**phone** | **str** | Phone number to be associated to the smart account | [optional] 

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


