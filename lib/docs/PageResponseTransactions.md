# PageResponseTransactions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Transaction]**](Transaction.md) |  | 
**page** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from openapi_client.models.page_response_transactions import PageResponseTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseTransactions from a JSON string
page_response_transactions_instance = PageResponseTransactions.from_json(json)
# print the JSON string representation of the object
print(PageResponseTransactions.to_json())

# convert the object into a dict
page_response_transactions_dict = page_response_transactions_instance.to_dict()
# create an instance of PageResponseTransactions from a dict
page_response_transactions_form_dict = page_response_transactions.from_dict(page_response_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


