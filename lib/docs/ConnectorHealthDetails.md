# ConnectorHealthDetails

Statistics about your recent connections on the connector and recent connection rate (percentage of healthy connections). This field is only present if you include the parameter healthDetails=true. This will be null if there was an error obtaining health details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_rate_last6_hours** | **float** | A number from 0 to 100: the percentage of executions that succesfully connect to the institution: status of CONNECTION_ERROR,ERROR,SITE_NOT_AVAILABLE decrease the percentage. Any other status (like SUCCESS/LOGIN_ERROR) increase the percentage. The value will be null if there were no connections | [optional] 
**connections_last6_hours** | **float** | Amount of your connections for this connector during the last 6 hours. 0 if there were no connections | [optional] 

## Example

```python
from openapi_client.models.connector_health_details import ConnectorHealthDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorHealthDetails from a JSON string
connector_health_details_instance = ConnectorHealthDetails.from_json(json)
# print the JSON string representation of the object
print(ConnectorHealthDetails.to_json())

# convert the object into a dict
connector_health_details_dict = connector_health_details_instance.to_dict()
# create an instance of ConnectorHealthDetails from a dict
connector_health_details_form_dict = connector_health_details.from_dict(connector_health_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


