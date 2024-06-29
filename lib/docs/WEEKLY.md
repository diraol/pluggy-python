# WEEKLY

Schedule atribute to generate weekly payments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**start_date** | **date** | The start date of the validity of the scheduled payment authorization. | 
**day_of_week** | **str** | Day of the week on which each payment will occur. For instance, if set to &#39;MONDAY&#39;, the first payment will occur on the first monday after the startDate (or the same day, if it is already monday), and every monday after that. | 
**occurrences** | **float** | Under the specified schedule frequency, how many payments will be scheduled to occur. | [optional] 

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


