# SmartAccountBalance

Smart account balance product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_at** | **datetime** | Balance date | 
**balance** | **float** | Smart account balance amount | 
**blocked_balance** | **float** | Smart account blocked balance amount | 
**scheduled_balance** | **float** | Smart account scheduled balance amount | 

## Example

```python
from pluggy_sdk.models.smart_account_balance import SmartAccountBalance

# TODO update the JSON string below
json = "{}"
# create an instance of SmartAccountBalance from a JSON string
smart_account_balance_instance = SmartAccountBalance.from_json(json)
# print the JSON string representation of the object
print(SmartAccountBalance.to_json())

# convert the object into a dict
smart_account_balance_dict = smart_account_balance_instance.to_dict()
# create an instance of SmartAccountBalance from a dict
smart_account_balance_form_dict = smart_account_balance.from_dict(smart_account_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


