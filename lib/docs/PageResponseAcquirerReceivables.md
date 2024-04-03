# PageResponseAcquirerReceivables



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AcquirerReceivable]**](AcquirerReceivable.md) |  | 
**page** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from openapi_client.models.page_response_acquirer_receivables import PageResponseAcquirerReceivables

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseAcquirerReceivables from a JSON string
page_response_acquirer_receivables_instance = PageResponseAcquirerReceivables.from_json(json)
# print the JSON string representation of the object
print(PageResponseAcquirerReceivables.to_json())

# convert the object into a dict
page_response_acquirer_receivables_dict = page_response_acquirer_receivables_instance.to_dict()
# create an instance of PageResponseAcquirerReceivables from a dict
page_response_acquirer_receivables_form_dict = page_response_acquirer_receivables.from_dict(page_response_acquirer_receivables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


