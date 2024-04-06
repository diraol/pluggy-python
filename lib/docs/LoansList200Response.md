# LoansList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[Loan]**](Loan.md) | List of loans | [optional] 

## Example

```python
from pluggy_sdk.models.loans_list200_response import LoansList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LoansList200Response from a JSON string
loans_list200_response_instance = LoansList200Response.from_json(json)
# print the JSON string representation of the object
print(LoansList200Response.to_json())

# convert the object into a dict
loans_list200_response_dict = loans_list200_response_instance.to_dict()
# create an instance of LoansList200Response from a dict
loans_list200_response_form_dict = loans_list200_response.from_dict(loans_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


