# AccountsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[Account]**](Account.md) | List of retrieved accounts | [optional] 

## Example

```python
from pluggy_sdk.models.accounts_list200_response import AccountsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsList200Response from a JSON string
accounts_list200_response_instance = AccountsList200Response.from_json(json)
# print the JSON string representation of the object
print(AccountsList200Response.to_json())

# convert the object into a dict
accounts_list200_response_dict = accounts_list200_response_instance.to_dict()
# create an instance of AccountsList200Response from a dict
accounts_list200_response_from_dict = AccountsList200Response.from_dict(accounts_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


