# EconomicActivity

CNAE code describing one of the business's economic activities. Only one entry per response should be marked as main

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | CNAE code (7 digits, including leading zeros). Follows the CNAE-Subclasse 2.3 classification | 
**is_main** | **bool** | Whether this is the main economic activity (true) or a secondary one (false). Only one item per response should be true | 

## Example

```python
from pluggy_sdk.models.economic_activity import EconomicActivity

# TODO update the JSON string below
json = "{}"
# create an instance of EconomicActivity from a JSON string
economic_activity_instance = EconomicActivity.from_json(json)
# print the JSON string representation of the object
print(EconomicActivity.to_json())

# convert the object into a dict
economic_activity_dict = economic_activity_instance.to_dict()
# create an instance of EconomicActivity from a dict
economic_activity_from_dict = EconomicActivity.from_dict(economic_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


