# IncomeReportsResponse

Response with the pages of metadata of the income reports files uploaded to Amazon S3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[IncomeReport]**](IncomeReport.md) | Array with the metadata of every income report | [optional] 

## Example

```python
from openapi_client.models.income_reports_response import IncomeReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncomeReportsResponse from a JSON string
income_reports_response_instance = IncomeReportsResponse.from_json(json)
# print the JSON string representation of the object
print(IncomeReportsResponse.to_json())

# convert the object into a dict
income_reports_response_dict = income_reports_response_instance.to_dict()
# create an instance of IncomeReportsResponse from a dict
income_reports_response_form_dict = income_reports_response.from_dict(income_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


