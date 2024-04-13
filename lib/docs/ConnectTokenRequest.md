# ConnectTokenRequest

Create a connect token request payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Item identifier to allow Connect Widget to performan an update on it. | [optional] 
**options** | [**ItemOptions**](ItemOptions.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.connect_token_request import ConnectTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectTokenRequest from a JSON string
connect_token_request_instance = ConnectTokenRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectTokenRequest.to_json())

# convert the object into a dict
connect_token_request_dict = connect_token_request_instance.to_dict()
# create an instance of ConnectTokenRequest from a dict
connect_token_request_from_dict = ConnectTokenRequest.from_dict(connect_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


