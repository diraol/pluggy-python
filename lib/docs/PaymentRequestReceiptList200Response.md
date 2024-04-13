# PaymentRequestReceiptList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[PaymentReceipt]**](PaymentReceipt.md) | List of payment receipts | [optional] 

## Example

```python
from pluggy_sdk.models.payment_request_receipt_list200_response import PaymentRequestReceiptList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestReceiptList200Response from a JSON string
payment_request_receipt_list200_response_instance = PaymentRequestReceiptList200Response.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestReceiptList200Response.to_json())

# convert the object into a dict
payment_request_receipt_list200_response_dict = payment_request_receipt_list200_response_instance.to_dict()
# create an instance of PaymentRequestReceiptList200Response from a dict
payment_request_receipt_list200_response_from_dict = PaymentRequestReceiptList200Response.from_dict(payment_request_receipt_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


