# NotAuthenticatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from pluggy_sdk.models.not_authenticated_response import NotAuthenticatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotAuthenticatedResponse from a JSON string
not_authenticated_response_instance = NotAuthenticatedResponse.from_json(json)
# print the JSON string representation of the object
print(NotAuthenticatedResponse.to_json())

# convert the object into a dict
not_authenticated_response_dict = not_authenticated_response_instance.to_dict()
# create an instance of NotAuthenticatedResponse from a dict
not_authenticated_response_from_dict = NotAuthenticatedResponse.from_dict(not_authenticated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


