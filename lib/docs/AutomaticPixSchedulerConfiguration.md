# AutomaticPixSchedulerConfiguration

Configuration for automatic scheduling of payments. When enabled, the system will schedule payments according to the consent interval and start date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | When true, payments are automatically scheduled by the system. | 
**description** | **str** | Optional description for the scheduled payment. Overrides the payment request description when set. | [optional] 
**value_for_variable_amount** | **float** | Required when the consent has variable amounts (minimumVariableAmount/maximumVariableAmount). Default amount to use when scheduling the payment. | [optional] 

## Example

```python
from pluggy_sdk.models.automatic_pix_scheduler_configuration import AutomaticPixSchedulerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AutomaticPixSchedulerConfiguration from a JSON string
automatic_pix_scheduler_configuration_instance = AutomaticPixSchedulerConfiguration.from_json(json)
# print the JSON string representation of the object
print(AutomaticPixSchedulerConfiguration.to_json())

# convert the object into a dict
automatic_pix_scheduler_configuration_dict = automatic_pix_scheduler_configuration_instance.to_dict()
# create an instance of AutomaticPixSchedulerConfiguration from a dict
automatic_pix_scheduler_configuration_from_dict = AutomaticPixSchedulerConfiguration.from_dict(automatic_pix_scheduler_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


