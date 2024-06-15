# PageResponseConsents



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Consent]**](Consent.md) |  | 
**page** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from pluggy_sdk.models.page_response_consents import PageResponseConsents

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseConsents from a JSON string
page_response_consents_instance = PageResponseConsents.from_json(json)
# print the JSON string representation of the object
print(PageResponseConsents.to_json())

# convert the object into a dict
page_response_consents_dict = page_response_consents_instance.to_dict()
# create an instance of PageResponseConsents from a dict
page_response_consents_from_dict = PageResponseConsents.from_dict(page_response_consents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


