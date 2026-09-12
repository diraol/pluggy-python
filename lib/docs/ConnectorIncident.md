# ConnectorIncident

An incident affecting a connector right now, as published on the Pluggy status page. Only incidents active at this moment are listed: a scheduled maintenance appears once its window opens, not when it is announced, and disappears when the window closes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Status page identifier of the incident | 
**title** | **str** | Short, customer-facing summary, for example &#39;XP Banking - Compras parceladas não sendo retornadas&#39; | 
**description** | **str** | Longer explanation, when there is one | [optional] 
**type** | **str** | What is broken, as opposed to how badly (severity) or how far along we are (state). Use it to group the same problem across institutions, and to decide which incidents are worth showing your own users: a SCHEDULED_MAINTENANCE and a TRANSACTIONS_MISSING both read as &#39;degraded&#39; otherwise. OTHER means Pluggy has not classified it, not that nothing is wrong | 
**product** | **str** | Which Pluggy product line the incident affects | 
**kind** | **str** | Whether this is an unplanned incident or a planned maintenance window | 
**severity** | **str** | How badly the institution is affected | 
**state** | **str** | Where the incident is in its lifecycle. Resolved incidents are not listed | 
**started_at** | **datetime** | When the incident began | 
**updated_at** | **datetime** | When the incident was last updated | [optional] 
**url** | **str** | Permalink to the incident on the status page, with its full timeline and postmortem. Safe to show to your own users | 

## Example

```python
from pluggy_sdk.models.connector_incident import ConnectorIncident

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorIncident from a JSON string
connector_incident_instance = ConnectorIncident.from_json(json)
# print the JSON string representation of the object
print(ConnectorIncident.to_json())

# convert the object into a dict
connector_incident_dict = connector_incident_instance.to_dict()
# create an instance of ConnectorIncident from a dict
connector_incident_from_dict = ConnectorIncident.from_dict(connector_incident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


