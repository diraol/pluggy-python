# ItemCreationErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**code_description** | **str** | Distinctive code description, useful to identify the error. | [optional] 
**message** | **str** |  | [optional] 
**errors** | [**List[ParameterValidationError]**](ParameterValidationError.md) | List of errors related to parameter validations | [optional] 

## Example

```python
from pluggy_sdk.models.item_creation_error_response import ItemCreationErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCreationErrorResponse from a JSON string
item_creation_error_response_instance = ItemCreationErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ItemCreationErrorResponse.to_json())

# convert the object into a dict
item_creation_error_response_dict = item_creation_error_response_instance.to_dict()
# create an instance of ItemCreationErrorResponse from a dict
item_creation_error_response_form_dict = item_creation_error_response.from_dict(item_creation_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


