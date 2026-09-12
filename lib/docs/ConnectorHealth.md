# ConnectorHealth

Connector health status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | &#39;ONLINE&#39; | &#39;OFFLINE&#39; | &#39;UNSTABLE&#39; | [optional] 
**stage** | **str** |  | [optional] 
**incidents** | [**List[ConnectorIncident]**](ConnectorIncident.md) | Incidents currently affecting this connector, as published on https://status.pluggy.ai. Absent when the connector has none, so a healthy connector&#39;s payload is unchanged. Ordered worst-first, so the first entry is the one to show if you only show one. Note this is about the institution, not about your own connections: use it to warn a user before they pick a bank that is known to be failing right now. | [optional] 
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


