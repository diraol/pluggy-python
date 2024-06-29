# CUSTOM

Schedule atribute to generate custom payments in the future

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**dates** | **List[date]** |  | 
**additional_information** | **str** | Additional information about the custom schedule | [optional] 

## Example

```python
from pluggy_sdk.models.custom import CUSTOM

# TODO update the JSON string below
json = "{}"
# create an instance of CUSTOM from a JSON string
custom_instance = CUSTOM.from_json(json)
# print the JSON string representation of the object
print(CUSTOM.to_json())

# convert the object into a dict
custom_dict = custom_instance.to_dict()
# create an instance of CUSTOM from a dict
custom_from_dict = CUSTOM.from_dict(custom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


