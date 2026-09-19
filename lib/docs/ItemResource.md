# ItemResource

One resource the financial institution declared for the item's Open Finance consent, reported verbatim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The institution&#39;s identifier for the resource. | [optional] 
**type** | **str** | Open Finance resource type. | [optional] 
**status** | **str** | What the institution reports about this resource. Note the British spelling of PENDING_AUTHORISATION: it is Open Finance&#39;s, kept verbatim. | [optional] 

## Example

```python
from pluggy_sdk.models.item_resource import ItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResource from a JSON string
item_resource_instance = ItemResource.from_json(json)
# print the JSON string representation of the object
print(ItemResource.to_json())

# convert the object into a dict
item_resource_dict = item_resource_instance.to_dict()
# create an instance of ItemResource from a dict
item_resource_from_dict = ItemResource.from_dict(item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


