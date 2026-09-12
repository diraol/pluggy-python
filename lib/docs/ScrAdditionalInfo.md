# ScrAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tp** | **str** | Type of the complementary information | [optional] 
**cd** | **str** | Code of the complementary information | [optional] 
**qtd** | **float** | Number of operations grouped under this entry | [optional] 

## Example

```python
from pluggy_sdk.models.scr_additional_info import ScrAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ScrAdditionalInfo from a JSON string
scr_additional_info_instance = ScrAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(ScrAdditionalInfo.to_json())

# convert the object into a dict
scr_additional_info_dict = scr_additional_info_instance.to_dict()
# create an instance of ScrAdditionalInfo from a dict
scr_additional_info_from_dict = ScrAdditionalInfo.from_dict(scr_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


