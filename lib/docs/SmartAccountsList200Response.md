# SmartAccountsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[SmartAccount]**](SmartAccount.md) | List of smart accounts | [optional] 

## Example

```python
from openapi_client.models.smart_accounts_list200_response import SmartAccountsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SmartAccountsList200Response from a JSON string
smart_accounts_list200_response_instance = SmartAccountsList200Response.from_json(json)
# print the JSON string representation of the object
print(SmartAccountsList200Response.to_json())

# convert the object into a dict
smart_accounts_list200_response_dict = smart_accounts_list200_response_instance.to_dict()
# create an instance of SmartAccountsList200Response from a dict
smart_accounts_list200_response_form_dict = smart_accounts_list200_response.from_dict(smart_accounts_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


