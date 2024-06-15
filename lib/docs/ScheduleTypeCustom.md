# ScheduleTypeCustom

Schedule atribute to generate custom payments in the future

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**dates** | **List[date]** |  | 
**additional_information** | **str** | Additional information about the custom schedule | [optional] 

## Example

```python
from pluggy_sdk.models.schedule_type_custom import ScheduleTypeCustom

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTypeCustom from a JSON string
schedule_type_custom_instance = ScheduleTypeCustom.from_json(json)
# print the JSON string representation of the object
print(ScheduleTypeCustom.to_json())

# convert the object into a dict
schedule_type_custom_dict = schedule_type_custom_instance.to_dict()
# create an instance of ScheduleTypeCustom from a dict
schedule_type_custom_from_dict = ScheduleTypeCustom.from_dict(schedule_type_custom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


