# InformedRevenue

Revenue (faturamento) informed by the business — the business equivalent of informedIncome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the informed revenue | 
**frequency** | **str** | Frequency or period of the informed revenue | [optional] 
**frequency_additional_info** | **str** | Free-text complement to the frequency. Populated when frequency is OTHER | [optional] 
**year** | **float** | Reference year of the revenue | [optional] 

## Example

```python
from pluggy_sdk.models.informed_revenue import InformedRevenue

# TODO update the JSON string below
json = "{}"
# create an instance of InformedRevenue from a JSON string
informed_revenue_instance = InformedRevenue.from_json(json)
# print the JSON string representation of the object
print(InformedRevenue.to_json())

# convert the object into a dict
informed_revenue_dict = informed_revenue_instance.to_dict()
# create an instance of InformedRevenue from a dict
informed_revenue_from_dict = InformedRevenue.from_dict(informed_revenue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


