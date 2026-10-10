# SmartTransferOverdraft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contracted** | **float** | Overdraft limit contracted, in BRL. | 
**used** | **float** | Part of the overdraft limit in use, in BRL. | 
**available** | **float** | Part of the overdraft limit still available, in BRL. | 

## Example

```python
from pluggy_sdk.models.smart_transfer_overdraft import SmartTransferOverdraft

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferOverdraft from a JSON string
smart_transfer_overdraft_instance = SmartTransferOverdraft.from_json(json)
# print the JSON string representation of the object
print(SmartTransferOverdraft.to_json())

# convert the object into a dict
smart_transfer_overdraft_dict = smart_transfer_overdraft_instance.to_dict()
# create an instance of SmartTransferOverdraft from a dict
smart_transfer_overdraft_from_dict = SmartTransferOverdraft.from_dict(smart_transfer_overdraft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


