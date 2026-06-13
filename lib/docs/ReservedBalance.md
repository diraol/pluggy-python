# ReservedBalance

Funds reserved/earmarked on a bank account (for example, goal-based savings or judicial holds)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User-given name for the reservation (for example, &#39;Caixinha Para Férias&#39;) | [optional] 
**identification** | **str** | Unique identifier of the reservation | 
**available_amounts** | [**List[ReservedBalanceAmount]**](ReservedBalanceAmount.md) | Available amount(s) in the reservation, one entry per remuneration band | 

## Example

```python
from pluggy_sdk.models.reserved_balance import ReservedBalance

# TODO update the JSON string below
json = "{}"
# create an instance of ReservedBalance from a JSON string
reserved_balance_instance = ReservedBalance.from_json(json)
# print the JSON string representation of the object
print(ReservedBalance.to_json())

# convert the object into a dict
reserved_balance_dict = reserved_balance_instance.to_dict()
# create an instance of ReservedBalance from a dict
reserved_balance_from_dict = ReservedBalance.from_dict(reserved_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


