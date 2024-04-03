# GlobalErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**code_description** | **str** | Distinctive code description, useful to distinguish the error. | [optional] 
**data** | **object** | Additional data related to the error, if any | [optional] 

## Example

```python
from openapi_client.models.global_error_response import GlobalErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalErrorResponse from a JSON string
global_error_response_instance = GlobalErrorResponse.from_json(json)
# print the JSON string representation of the object
print(GlobalErrorResponse.to_json())

# convert the object into a dict
global_error_response_dict = global_error_response_instance.to_dict()
# create an instance of GlobalErrorResponse from a dict
global_error_response_form_dict = global_error_response.from_dict(global_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


