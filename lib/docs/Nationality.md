# Nationality

Nationality of the natural person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_brazilian_nationality** | **bool** | Whether the client has Brazilian nationality | 
**other_nationalities** | [**List[NationalityOtherNationalitiesInner]**](NationalityOtherNationalitiesInner.md) | Other nationalities held by the client, if any | [optional] 

## Example

```python
from pluggy_sdk.models.nationality import Nationality

# TODO update the JSON string below
json = "{}"
# create an instance of Nationality from a JSON string
nationality_instance = Nationality.from_json(json)
# print the JSON string representation of the object
print(Nationality.to_json())

# convert the object into a dict
nationality_dict = nationality_instance.to_dict()
# create an instance of Nationality from a dict
nationality_from_dict = Nationality.from_dict(nationality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


