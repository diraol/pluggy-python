# NationalityOtherNationalitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Country code in alpha3 ISO-3166 format | 
**documents** | [**List[NationalityDocument]**](NationalityDocument.md) | Supporting documents for this nationality | 

## Example

```python
from pluggy_sdk.models.nationality_other_nationalities_inner import NationalityOtherNationalitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of NationalityOtherNationalitiesInner from a JSON string
nationality_other_nationalities_inner_instance = NationalityOtherNationalitiesInner.from_json(json)
# print the JSON string representation of the object
print(NationalityOtherNationalitiesInner.to_json())

# convert the object into a dict
nationality_other_nationalities_inner_dict = nationality_other_nationalities_inner_instance.to_dict()
# create an instance of NationalityOtherNationalitiesInner from a dict
nationality_other_nationalities_inner_from_dict = NationalityOtherNationalitiesInner.from_dict(nationality_other_nationalities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


