# ScrGuarantee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tp** | **str** | Bacen&#39;s code for the guarantee type | [optional] 
**qtd** | **float** | Number of operations grouped under this type | [optional] 

## Example

```python
from pluggy_sdk.models.scr_guarantee import ScrGuarantee

# TODO update the JSON string below
json = "{}"
# create an instance of ScrGuarantee from a JSON string
scr_guarantee_instance = ScrGuarantee.from_json(json)
# print the JSON string representation of the object
print(ScrGuarantee.to_json())

# convert the object into a dict
scr_guarantee_dict = scr_guarantee_instance.to_dict()
# create an instance of ScrGuarantee from a dict
scr_guarantee_from_dict = ScrGuarantee.from_dict(scr_guarantee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


