# MONTHLY

Schedule atribute to generate monthly payments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Scheduled type | 
**start_date** | **date** |  | 
**day_of_month** | **float** | Day of the month on which each payment will occur. For example, if &#39;10&#39;, the first payment will occur on the next 10th day of the month after the start date, or the same day if it is already 10th, and every 10th day after that. | 
**occurrences** | **float** | Under the specified schedule frequency, how many payments will be scheduled to occur. | [optional] 

## Example

```python
from pluggy_sdk.models.monthly import MONTHLY

# TODO update the JSON string below
json = "{}"
# create an instance of MONTHLY from a JSON string
monthly_instance = MONTHLY.from_json(json)
# print the JSON string representation of the object
print(MONTHLY.to_json())

# convert the object into a dict
monthly_dict = monthly_instance.to_dict()
# create an instance of MONTHLY from a dict
monthly_from_dict = MONTHLY.from_dict(monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


