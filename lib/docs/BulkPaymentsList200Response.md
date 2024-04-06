# BulkPaymentsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[BulkPayment]**](BulkPayment.md) | List of bulk payments | [optional] 

## Example

```python
from pluggy_sdk.models.bulk_payments_list200_response import BulkPaymentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPaymentsList200Response from a JSON string
bulk_payments_list200_response_instance = BulkPaymentsList200Response.from_json(json)
# print the JSON string representation of the object
print(BulkPaymentsList200Response.to_json())

# convert the object into a dict
bulk_payments_list200_response_dict = bulk_payments_list200_response_instance.to_dict()
# create an instance of BulkPaymentsList200Response from a dict
bulk_payments_list200_response_form_dict = bulk_payments_list200_response.from_dict(bulk_payments_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


