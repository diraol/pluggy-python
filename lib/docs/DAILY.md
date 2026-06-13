# DAILY

Schedule attribute to generate daily payments starting from `startDate`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Schedule discriminator. Always &#x60;DAILY&#x60; for this variant. | 
**start_date** | **date** | The start date of the validity of the scheduled payment authorization. | 
**occurrences** | **float** | Under the specified schedule frequency, how many payments will be scheduled to occur. | 

## Example

```python
from pluggy_sdk.models.daily import DAILY

# TODO update the JSON string below
json = "{}"
# create an instance of DAILY from a JSON string
daily_instance = DAILY.from_json(json)
# print the JSON string representation of the object
print(DAILY.to_json())

# convert the object into a dict
daily_dict = daily_instance.to_dict()
# create an instance of DAILY from a dict
daily_from_dict = DAILY.from_dict(daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


