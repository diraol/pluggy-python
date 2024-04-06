# BillsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[Bill]**](Bill.md) | List of credit card bills | [optional] 

## Example

```python
from pluggy_sdk.models.bills_list200_response import BillsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillsList200Response from a JSON string
bills_list200_response_instance = BillsList200Response.from_json(json)
# print the JSON string representation of the object
print(BillsList200Response.to_json())

# convert the object into a dict
bills_list200_response_dict = bills_list200_response_instance.to_dict()
# create an instance of BillsList200Response from a dict
bills_list200_response_form_dict = bills_list200_response.from_dict(bills_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


