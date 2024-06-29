# SINGLE

Schedule atribute to generate one payment in the future

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**var_date** | **date** |  | 

## Example

```python
from pluggy_sdk.models.single import SINGLE

# TODO update the JSON string below
json = "{}"
# create an instance of SINGLE from a JSON string
single_instance = SINGLE.from_json(json)
# print the JSON string representation of the object
print(SINGLE.to_json())

# convert the object into a dict
single_dict = single_instance.to_dict()
# create an instance of SINGLE from a dict
single_from_dict = SINGLE.from_dict(single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


