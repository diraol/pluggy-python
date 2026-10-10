# SmartTransferPreauthorizationBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Source account balance in BRL. | 
**overdraft** | [**SmartTransferOverdraft**](SmartTransferOverdraft.md) | Overdraft limit of the source account. Null when the institution does not share it. | 

## Example

```python
from pluggy_sdk.models.smart_transfer_preauthorization_balance import SmartTransferPreauthorizationBalance

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPreauthorizationBalance from a JSON string
smart_transfer_preauthorization_balance_instance = SmartTransferPreauthorizationBalance.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPreauthorizationBalance.to_json())

# convert the object into a dict
smart_transfer_preauthorization_balance_dict = smart_transfer_preauthorization_balance_instance.to_dict()
# create an instance of SmartTransferPreauthorizationBalance from a dict
smart_transfer_preauthorization_balance_from_dict = SmartTransferPreauthorizationBalance.from_dict(smart_transfer_preauthorization_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


