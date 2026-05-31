# PhoneNumber

The phone number object contains data related to contact information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of phone number: personal, work or residencial | [optional] 
**value** | **str** | The complete phone number | 
**country_calling_code** | **str** | International dialing code (DDI). Populated when different from &#39;55&#39; | [optional] 
**area_code** | **str** | Area code (DDD) of the client&#39;s phone | [optional] 
**extension** | **str** | Extension number, when part of the phone identification | [optional] 
**additional_info** | **str** | Additional info related to the source phone type. Populated when the source type at the institution does not fit the standard categories | [optional] 

## Example

```python
from pluggy_sdk.models.phone_number import PhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumber from a JSON string
phone_number_instance = PhoneNumber.from_json(json)
# print the JSON string representation of the object
print(PhoneNumber.to_json())

# convert the object into a dict
phone_number_dict = phone_number_instance.to_dict()
# create an instance of PhoneNumber from a dict
phone_number_from_dict = PhoneNumber.from_dict(phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


