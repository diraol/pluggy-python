# CursorPageResponseItems

Cursor-based paginated response for items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Item]**](Item.md) | List of items for the current page | 
**next** | **str** | Ready-to-use query string for the next page: append it as-is to the endpoint path (GET /v2/items{next}). Null if there are no more results. | 

## Example

```python
from pluggy_sdk.models.cursor_page_response_items import CursorPageResponseItems

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPageResponseItems from a JSON string
cursor_page_response_items_instance = CursorPageResponseItems.from_json(json)
# print the JSON string representation of the object
print(CursorPageResponseItems.to_json())

# convert the object into a dict
cursor_page_response_items_dict = cursor_page_response_items_instance.to_dict()
# create an instance of CursorPageResponseItems from a dict
cursor_page_response_items_from_dict = CursorPageResponseItems.from_dict(cursor_page_response_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


