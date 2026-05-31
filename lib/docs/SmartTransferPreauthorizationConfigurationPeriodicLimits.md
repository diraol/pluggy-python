# SmartTransferPreauthorizationConfigurationPeriodicLimits

Transactional limits per period as determined by the paying user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | [**SmartTransferPreauthorizationConfigurationPeriodicLimit**](SmartTransferPreauthorizationConfigurationPeriodicLimit.md) | Daily transactional limit. | [optional] 
**week** | [**SmartTransferPreauthorizationConfigurationPeriodicLimit**](SmartTransferPreauthorizationConfigurationPeriodicLimit.md) | Weekly transactional limit. | [optional] 
**month** | [**SmartTransferPreauthorizationConfigurationPeriodicLimit**](SmartTransferPreauthorizationConfigurationPeriodicLimit.md) | Monthly transactional limit. | [optional] 
**year** | [**SmartTransferPreauthorizationConfigurationPeriodicLimit**](SmartTransferPreauthorizationConfigurationPeriodicLimit.md) | Yearly transactional limit. | [optional] 

## Example

```python
from pluggy_sdk.models.smart_transfer_preauthorization_configuration_periodic_limits import SmartTransferPreauthorizationConfigurationPeriodicLimits

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPreauthorizationConfigurationPeriodicLimits from a JSON string
smart_transfer_preauthorization_configuration_periodic_limits_instance = SmartTransferPreauthorizationConfigurationPeriodicLimits.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPreauthorizationConfigurationPeriodicLimits.to_json())

# convert the object into a dict
smart_transfer_preauthorization_configuration_periodic_limits_dict = smart_transfer_preauthorization_configuration_periodic_limits_instance.to_dict()
# create an instance of SmartTransferPreauthorizationConfigurationPeriodicLimits from a dict
smart_transfer_preauthorization_configuration_periodic_limits_from_dict = SmartTransferPreauthorizationConfigurationPeriodicLimits.from_dict(smart_transfer_preauthorization_configuration_periodic_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


