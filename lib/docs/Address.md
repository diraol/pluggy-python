# Address

The address object contains data related to an specific owner's location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_address** | **str** | Full address using all components available | [optional] 
**primary_address** | **str** | Primary address, stret name and street number | [optional] 
**city** | **str** | The complete city name | [optional] 
**postal_code** | **str** | The Zip code | [optional] 
**state** | **str** | The state or province | [optional] 
**country** | **str** | The complete country name | [optional] 
**type** | **str** | Type of address, Personal or Work | [optional] 

## Example

```python
from openapi_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_form_dict = address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


