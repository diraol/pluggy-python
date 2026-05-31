# SmartTransferPreauthorizationConfiguration

Smart transfer preauthorization configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_allowed_amount** | **float** | Maximum amount to be reached by the sum of all transactions that use the consent authorized by the customer. | [optional] 
**transaction_limit** | **float** | Maximum amount for each payment transaction associated with this consent. | [optional] 
**periodic_limits** | [**SmartTransferPreauthorizationConfigurationPeriodicLimits**](SmartTransferPreauthorizationConfigurationPeriodicLimits.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.smart_transfer_preauthorization_configuration import SmartTransferPreauthorizationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPreauthorizationConfiguration from a JSON string
smart_transfer_preauthorization_configuration_instance = SmartTransferPreauthorizationConfiguration.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPreauthorizationConfiguration.to_json())

# convert the object into a dict
smart_transfer_preauthorization_configuration_dict = smart_transfer_preauthorization_configuration_instance.to_dict()
# create an instance of SmartTransferPreauthorizationConfiguration from a dict
smart_transfer_preauthorization_configuration_from_dict = SmartTransferPreauthorizationConfiguration.from_dict(smart_transfer_preauthorization_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


