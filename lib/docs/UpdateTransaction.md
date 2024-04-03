# UpdateTransaction

Update transaction category request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | Identifier of the category | 

## Example

```python
from openapi_client.models.update_transaction import UpdateTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransaction from a JSON string
update_transaction_instance = UpdateTransaction.from_json(json)
# print the JSON string representation of the object
print(UpdateTransaction.to_json())

# convert the object into a dict
update_transaction_dict = update_transaction_instance.to_dict()
# create an instance of UpdateTransaction from a dict
update_transaction_form_dict = update_transaction.from_dict(update_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


