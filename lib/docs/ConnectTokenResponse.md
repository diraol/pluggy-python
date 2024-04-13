# ConnectTokenResponse

Connect token response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Connect token that&#39;s used to initialize Pluggy&#39;s Connect widget | 

## Example

```python
from pluggy_sdk.models.connect_token_response import ConnectTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectTokenResponse from a JSON string
connect_token_response_instance = ConnectTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectTokenResponse.to_json())

# convert the object into a dict
connect_token_response_dict = connect_token_response_instance.to_dict()
# create an instance of ConnectTokenResponse from a dict
connect_token_response_from_dict = ConnectTokenResponse.from_dict(connect_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


