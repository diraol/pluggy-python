# PageResponseAcquirerSales



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AcquirerSale]**](AcquirerSale.md) |  | 
**page** | **float** |  | 
**total** | **float** |  | 
**total_pages** | **float** |  | 

## Example

```python
from pluggy_sdk.models.page_response_acquirer_sales import PageResponseAcquirerSales

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseAcquirerSales from a JSON string
page_response_acquirer_sales_instance = PageResponseAcquirerSales.from_json(json)
# print the JSON string representation of the object
print(PageResponseAcquirerSales.to_json())

# convert the object into a dict
page_response_acquirer_sales_dict = page_response_acquirer_sales_instance.to_dict()
# create an instance of PageResponseAcquirerSales from a dict
page_response_acquirer_sales_form_dict = page_response_acquirer_sales.from_dict(page_response_acquirer_sales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


