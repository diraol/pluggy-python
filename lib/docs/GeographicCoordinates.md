# GeographicCoordinates

Geographic coordinates in decimal degrees, WGS84 reference system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. Between -90 and 90 (e.g. -23.5475) | 
**longitude** | **float** | Longitude. Between -180 and 180 (e.g. -46.6361) | 

## Example

```python
from pluggy_sdk.models.geographic_coordinates import GeographicCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of GeographicCoordinates from a JSON string
geographic_coordinates_instance = GeographicCoordinates.from_json(json)
# print the JSON string representation of the object
print(GeographicCoordinates.to_json())

# convert the object into a dict
geographic_coordinates_dict = geographic_coordinates_instance.to_dict()
# create an instance of GeographicCoordinates from a dict
geographic_coordinates_from_dict = GeographicCoordinates.from_dict(geographic_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


