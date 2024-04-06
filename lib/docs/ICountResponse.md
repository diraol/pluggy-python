# ICountResponse

Deletion response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **float** | Amount of items deleted | 

## Example

```python
from pluggy_sdk.models.i_count_response import ICountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ICountResponse from a JSON string
i_count_response_instance = ICountResponse.from_json(json)
# print the JSON string representation of the object
print(ICountResponse.to_json())

# convert the object into a dict
i_count_response_dict = i_count_response_instance.to_dict()
# create an instance of ICountResponse from a dict
i_count_response_form_dict = i_count_response.from_dict(i_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


