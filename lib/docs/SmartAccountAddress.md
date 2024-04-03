# SmartAccountAddress

Smart account owner address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type** | **str** | Owner address type | [optional] 
**postal_code** | **str** | Owner address postal code | [optional] 
**street_name** | **str** | Owner address street name | [optional] 
**street_number** | **str** | Owner address street number | [optional] 
**city** | **str** | Owner address city | 
**state** | **str** | Owner address state | [optional] 
**is_primary_address** | **bool** | Indicates if the owner address is the primary one | [optional] 
**is_mailing_address** | **bool** | Indicates if the owner address is the mailing one | [optional] 

## Example

```python
from openapi_client.models.smart_account_address import SmartAccountAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SmartAccountAddress from a JSON string
smart_account_address_instance = SmartAccountAddress.from_json(json)
# print the JSON string representation of the object
print(SmartAccountAddress.to_json())

# convert the object into a dict
smart_account_address_dict = smart_account_address_instance.to_dict()
# create an instance of SmartAccountAddress from a dict
smart_account_address_form_dict = smart_account_address.from_dict(smart_account_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


