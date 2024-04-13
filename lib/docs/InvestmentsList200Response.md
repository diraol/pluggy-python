# InvestmentsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[Investment]**](Investment.md) | List of investments | [optional] 

## Example

```python
from pluggy_sdk.models.investments_list200_response import InvestmentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentsList200Response from a JSON string
investments_list200_response_instance = InvestmentsList200Response.from_json(json)
# print the JSON string representation of the object
print(InvestmentsList200Response.to_json())

# convert the object into a dict
investments_list200_response_dict = investments_list200_response_instance.to_dict()
# create an instance of InvestmentsList200Response from a dict
investments_list200_response_from_dict = InvestmentsList200Response.from_dict(investments_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


