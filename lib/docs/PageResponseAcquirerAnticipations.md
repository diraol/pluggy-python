# PageResponseAcquirerAnticipations



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AcquirerAnticipation]**](AcquirerAnticipation.md) |  | 
**page** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from pluggy_sdk.models.page_response_acquirer_anticipations import PageResponseAcquirerAnticipations

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseAcquirerAnticipations from a JSON string
page_response_acquirer_anticipations_instance = PageResponseAcquirerAnticipations.from_json(json)
# print the JSON string representation of the object
print(PageResponseAcquirerAnticipations.to_json())

# convert the object into a dict
page_response_acquirer_anticipations_dict = page_response_acquirer_anticipations_instance.to_dict()
# create an instance of PageResponseAcquirerAnticipations from a dict
page_response_acquirer_anticipations_form_dict = page_response_acquirer_anticipations.from_dict(page_response_acquirer_anticipations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


