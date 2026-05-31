# CursorPageResponseTransactions

Cursor-based paginated response for transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Transaction]**](Transaction.md) | List of transactions for the current page | 
**next** | **str** | Query string for the next page of results. Null if there are no more results. | 

## Example

```python
from pluggy_sdk.models.cursor_page_response_transactions import CursorPageResponseTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPageResponseTransactions from a JSON string
cursor_page_response_transactions_instance = CursorPageResponseTransactions.from_json(json)
# print the JSON string representation of the object
print(CursorPageResponseTransactions.to_json())

# convert the object into a dict
cursor_page_response_transactions_dict = cursor_page_response_transactions_instance.to_dict()
# create an instance of CursorPageResponseTransactions from a dict
cursor_page_response_transactions_from_dict = CursorPageResponseTransactions.from_dict(cursor_page_response_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


