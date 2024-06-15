# ScheduleTypeSingle

Schedule atribute to generate one payment in the future

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**var_date** | **date** |  | 

## Example

```python
from pluggy_sdk.models.schedule_type_single import ScheduleTypeSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTypeSingle from a JSON string
schedule_type_single_instance = ScheduleTypeSingle.from_json(json)
# print the JSON string representation of the object
print(ScheduleTypeSingle.to_json())

# convert the object into a dict
schedule_type_single_dict = schedule_type_single_instance.to_dict()
# create an instance of ScheduleTypeSingle from a dict
schedule_type_single_from_dict = ScheduleTypeSingle.from_dict(schedule_type_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


