# ConnectorHealth

Connector health status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | &#39;ONLINE&#39; | &#39;OFFLINE&#39; | &#39;UNSTABLE&#39; | [optional] 
**stage** | **str** |  | [optional] 
**details** | [**ConnectorHealthDetails**](ConnectorHealthDetails.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.connector_health import ConnectorHealth

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorHealth from a JSON string
connector_health_instance = ConnectorHealth.from_json(json)
# print the JSON string representation of the object
print(ConnectorHealth.to_json())

# convert the object into a dict
connector_health_dict = connector_health_instance.to_dict()
# create an instance of ConnectorHealth from a dict
connector_health_from_dict = ConnectorHealth.from_dict(connector_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


