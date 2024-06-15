# PayrollLoansList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[PayrollLoanResponse]**](PayrollLoanResponse.md) | List of payroll loans | [optional] 

## Example

```python
from pluggy_sdk.models.payroll_loans_list200_response import PayrollLoansList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollLoansList200Response from a JSON string
payroll_loans_list200_response_instance = PayrollLoansList200Response.from_json(json)
# print the JSON string representation of the object
print(PayrollLoansList200Response.to_json())

# convert the object into a dict
payroll_loans_list200_response_dict = payroll_loans_list200_response_instance.to_dict()
# create an instance of PayrollLoansList200Response from a dict
payroll_loans_list200_response_from_dict = PayrollLoansList200Response.from_dict(payroll_loans_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


