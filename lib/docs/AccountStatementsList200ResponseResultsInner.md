# AccountStatementsList200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**month_year** | **str** |  | 
**url** | **str** | Signed URL to the statement file, this url is valid for 30 minutes | 

## Example

```python
from pluggy_sdk.models.account_statements_list200_response_results_inner import AccountStatementsList200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatementsList200ResponseResultsInner from a JSON string
account_statements_list200_response_results_inner_instance = AccountStatementsList200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(AccountStatementsList200ResponseResultsInner.to_json())

# convert the object into a dict
account_statements_list200_response_results_inner_dict = account_statements_list200_response_results_inner_instance.to_dict()
# create an instance of AccountStatementsList200ResponseResultsInner from a dict
account_statements_list200_response_results_inner_from_dict = AccountStatementsList200ResponseResultsInner.from_dict(account_statements_list200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


