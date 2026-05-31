# AutomaticPixRetriesConfiguration

“Configuration for automatic retries. If provided, the scheduled payments associated with this consent will only be retried on the days specified in the array after the original payment date. This does not apply to the first payment, only for scheduled payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry_days** | **List[int]** |  | 

## Example

```python
from pluggy_sdk.models.automatic_pix_retries_configuration import AutomaticPixRetriesConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AutomaticPixRetriesConfiguration from a JSON string
automatic_pix_retries_configuration_instance = AutomaticPixRetriesConfiguration.from_json(json)
# print the JSON string representation of the object
print(AutomaticPixRetriesConfiguration.to_json())

# convert the object into a dict
automatic_pix_retries_configuration_dict = automatic_pix_retries_configuration_instance.to_dict()
# create an instance of AutomaticPixRetriesConfiguration from a dict
automatic_pix_retries_configuration_from_dict = AutomaticPixRetriesConfiguration.from_dict(automatic_pix_retries_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


