# ScheduleTypeMonthly

Schedule atribute to generate weekly payments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**start_date** | **date** |  | 
**day_of_month** | **float** | Day of the mont to generate the payment | 
**quantity** | **float** |  | 

## Example

```python
from pluggy_sdk.models.schedule_type_monthly import ScheduleTypeMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTypeMonthly from a JSON string
schedule_type_monthly_instance = ScheduleTypeMonthly.from_json(json)
# print the JSON string representation of the object
print(ScheduleTypeMonthly.to_json())

# convert the object into a dict
schedule_type_monthly_dict = schedule_type_monthly_instance.to_dict()
# create an instance of ScheduleTypeMonthly from a dict
schedule_type_monthly_from_dict = ScheduleTypeMonthly.from_dict(schedule_type_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


