# PaymentRequestsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[PaymentRequest]**](PaymentRequest.md) | List of payment requests | [optional] 

## Example

```python
from pluggy_sdk.models.payment_requests_list200_response import PaymentRequestsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestsList200Response from a JSON string
payment_requests_list200_response_instance = PaymentRequestsList200Response.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestsList200Response.to_json())

# convert the object into a dict
payment_requests_list200_response_dict = payment_requests_list200_response_instance.to_dict()
# create an instance of PaymentRequestsList200Response from a dict
payment_requests_list200_response_form_dict = payment_requests_list200_response.from_dict(payment_requests_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


