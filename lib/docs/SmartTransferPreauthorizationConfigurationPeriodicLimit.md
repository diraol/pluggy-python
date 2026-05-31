# SmartTransferPreauthorizationConfigurationPeriodicLimit

Transactional limit per period. If sent, at least one of the fields (quantityLimit or transactionLimit) must be filled in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity_limit** | **float** | Maximum number of transactions allowed to occur in the period. | [optional] 
**transaction_limit** | **float** | Maximum amount to be transacted in the period. | [optional] 

## Example

```python
from pluggy_sdk.models.smart_transfer_preauthorization_configuration_periodic_limit import SmartTransferPreauthorizationConfigurationPeriodicLimit

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPreauthorizationConfigurationPeriodicLimit from a JSON string
smart_transfer_preauthorization_configuration_periodic_limit_instance = SmartTransferPreauthorizationConfigurationPeriodicLimit.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPreauthorizationConfigurationPeriodicLimit.to_json())

# convert the object into a dict
smart_transfer_preauthorization_configuration_periodic_limit_dict = smart_transfer_preauthorization_configuration_periodic_limit_instance.to_dict()
# create an instance of SmartTransferPreauthorizationConfigurationPeriodicLimit from a dict
smart_transfer_preauthorization_configuration_periodic_limit_from_dict = SmartTransferPreauthorizationConfigurationPeriodicLimit.from_dict(smart_transfer_preauthorization_configuration_periodic_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


