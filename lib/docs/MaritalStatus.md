# MaritalStatus

Marital status of the natural person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Marital status code | 
**additional_info** | **str** | Free-text complement. Populated when code is OTHER | [optional] 

## Example

```python
from pluggy_sdk.models.marital_status import MaritalStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MaritalStatus from a JSON string
marital_status_instance = MaritalStatus.from_json(json)
# print the JSON string representation of the object
print(MaritalStatus.to_json())

# convert the object into a dict
marital_status_dict = marital_status_instance.to_dict()
# create an instance of MaritalStatus from a dict
marital_status_from_dict = MaritalStatus.from_dict(marital_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


