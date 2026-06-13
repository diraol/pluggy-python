# WEEKLY

Schedule attribute to generate weekly payments on a specific day of the week.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Schedule discriminator. Always &#x60;WEEKLY&#x60; for this variant. | 
**start_date** | **date** | The start date of the validity of the scheduled payment authorization. | 
**day_of_week** | **str** | Day of the week on which each payment will occur. For instance, if set to &#x60;MONDAY&#x60;, the first payment will occur on the first Monday after &#x60;startDate&#x60; (or the same day, if it is already Monday), and every Monday after that. | 
**occurrences** | **float** | Under the specified schedule frequency, how many payments will be scheduled to occur. | 

## Example

```python
from pluggy_sdk.models.weekly import WEEKLY

# TODO update the JSON string below
json = "{}"
# create an instance of WEEKLY from a JSON string
weekly_instance = WEEKLY.from_json(json)
# print the JSON string representation of the object
print(WEEKLY.to_json())

# convert the object into a dict
weekly_dict = weekly_instance.to_dict()
# create an instance of WEEKLY from a dict
weekly_from_dict = WEEKLY.from_dict(weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


