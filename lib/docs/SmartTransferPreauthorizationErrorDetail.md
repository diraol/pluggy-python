# SmartTransferPreauthorizationErrorDetail

Error detail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code | [optional] 
**description** | **str** | Error description | [optional] 
**detail** | **str** | Error detail | [optional] 

## Example

```python
from pluggy_sdk.models.smart_transfer_preauthorization_error_detail import SmartTransferPreauthorizationErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPreauthorizationErrorDetail from a JSON string
smart_transfer_preauthorization_error_detail_instance = SmartTransferPreauthorizationErrorDetail.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPreauthorizationErrorDetail.to_json())

# convert the object into a dict
smart_transfer_preauthorization_error_detail_dict = smart_transfer_preauthorization_error_detail_instance.to_dict()
# create an instance of SmartTransferPreauthorizationErrorDetail from a dict
smart_transfer_preauthorization_error_detail_from_dict = SmartTransferPreauthorizationErrorDetail.from_dict(smart_transfer_preauthorization_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


