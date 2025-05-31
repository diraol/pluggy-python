# AdditionalCard

Additional credit card data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number of the additional credit card | 

## Example

```python
from pluggy_sdk.models.additional_card import AdditionalCard

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalCard from a JSON string
additional_card_instance = AdditionalCard.from_json(json)
# print the JSON string representation of the object
print(AdditionalCard.to_json())

# convert the object into a dict
additional_card_dict = additional_card_instance.to_dict()
# create an instance of AdditionalCard from a dict
additional_card_from_dict = AdditionalCard.from_dict(additional_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


