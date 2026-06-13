# ReservedBalanceAmount

A single amount within a reserved balance, optionally with its remuneration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Reserved amount | 
**currency_code** | **str** | Amount currency code (for example, BRL) | 
**remuneration** | [**ReservedBalanceRemuneration**](ReservedBalanceRemuneration.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.reserved_balance_amount import ReservedBalanceAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ReservedBalanceAmount from a JSON string
reserved_balance_amount_instance = ReservedBalanceAmount.from_json(json)
# print the JSON string representation of the object
print(ReservedBalanceAmount.to_json())

# convert the object into a dict
reserved_balance_amount_dict = reserved_balance_amount_instance.to_dict()
# create an instance of ReservedBalanceAmount from a dict
reserved_balance_amount_from_dict = ReservedBalanceAmount.from_dict(reserved_balance_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


