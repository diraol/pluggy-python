# IncomeReport

Income report entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the income report file available to be downloaded from Amazon S3 | [optional] 
**year** | **float** | Year to which the income report belongs | [optional] 

## Example

```python
from pluggy_sdk.models.income_report import IncomeReport

# TODO update the JSON string below
json = "{}"
# create an instance of IncomeReport from a JSON string
income_report_instance = IncomeReport.from_json(json)
# print the JSON string representation of the object
print(IncomeReport.to_json())

# convert the object into a dict
income_report_dict = income_report_instance.to_dict()
# create an instance of IncomeReport from a dict
income_report_from_dict = IncomeReport.from_dict(income_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


