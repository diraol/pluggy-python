# ItemsResources200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[ItemResource]**](ItemResource.md) | List of declared resources | [optional] 

## Example

```python
from pluggy_sdk.models.items_resources200_response import ItemsResources200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsResources200Response from a JSON string
items_resources200_response_instance = ItemsResources200Response.from_json(json)
# print the JSON string representation of the object
print(ItemsResources200Response.to_json())

# convert the object into a dict
items_resources200_response_dict = items_resources200_response_instance.to_dict()
# create an instance of ItemsResources200Response from a dict
items_resources200_response_from_dict = ItemsResources200Response.from_dict(items_resources200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


