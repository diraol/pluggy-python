# AccountStatementsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**total_pages** | **float** |  | 
**page** | **float** |  | 
**results** | [**List[AccountStatementsList200ResponseResultsInner]**](AccountStatementsList200ResponseResultsInner.md) |  | 

## Example

```python
from pluggy_sdk.models.account_statements_list200_response import AccountStatementsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatementsList200Response from a JSON string
account_statements_list200_response_instance = AccountStatementsList200Response.from_json(json)
# print the JSON string representation of the object
print(AccountStatementsList200Response.to_json())

# convert the object into a dict
account_statements_list200_response_dict = account_statements_list200_response_instance.to_dict()
# create an instance of AccountStatementsList200Response from a dict
account_statements_list200_response_from_dict = AccountStatementsList200Response.from_dict(account_statements_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


