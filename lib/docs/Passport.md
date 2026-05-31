# Passport

Passport metadata for the natural person. Applies when the client is a non-resident not required to register a CPF

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Passport number | 
**country** | **str** | Issuing country in alpha3 ISO-3166 format | 
**issue_date** | **datetime** | Issue date of the passport | [optional] 
**expiration_date** | **datetime** | Expiration date of the passport | [optional] 

## Example

```python
from pluggy_sdk.models.passport import Passport

# TODO update the JSON string below
json = "{}"
# create an instance of Passport from a JSON string
passport_instance = Passport.from_json(json)
# print the JSON string representation of the object
print(Passport.to_json())

# convert the object into a dict
passport_dict = passport_instance.to_dict()
# create an instance of Passport from a dict
passport_from_dict = Passport.from_dict(passport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


