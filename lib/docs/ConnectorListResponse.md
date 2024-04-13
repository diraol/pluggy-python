# ConnectorListResponse

Connector List Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[Connector]**](Connector.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.connector_list_response import ConnectorListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorListResponse from a JSON string
connector_list_response_instance = ConnectorListResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectorListResponse.to_json())

# convert the object into a dict
connector_list_response_dict = connector_list_response_instance.to_dict()
# create an instance of ConnectorListResponse from a dict
connector_list_response_from_dict = ConnectorListResponse.from_dict(connector_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


