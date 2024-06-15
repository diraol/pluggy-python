# ScheduleTypeDaily

Schedule atribute to generate daily payments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**start_date** | **date** |  | 
**quantity** | **float** |  | 

## Example

```python
from pluggy_sdk.models.schedule_type_daily import ScheduleTypeDaily

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTypeDaily from a JSON string
schedule_type_daily_instance = ScheduleTypeDaily.from_json(json)
# print the JSON string representation of the object
print(ScheduleTypeDaily.to_json())

# convert the object into a dict
schedule_type_daily_dict = schedule_type_daily_instance.to_dict()
# create an instance of ScheduleTypeDaily from a dict
schedule_type_daily_from_dict = ScheduleTypeDaily.from_dict(schedule_type_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


