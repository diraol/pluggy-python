# PaymentCustomersList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[PaymentCustomer]**](PaymentCustomer.md) | List of payment customers | [optional] 

## Example

```python
from pluggy_sdk.models.payment_customers_list200_response import PaymentCustomersList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCustomersList200Response from a JSON string
payment_customers_list200_response_instance = PaymentCustomersList200Response.from_json(json)
# print the JSON string representation of the object
print(PaymentCustomersList200Response.to_json())

# convert the object into a dict
payment_customers_list200_response_dict = payment_customers_list200_response_instance.to_dict()
# create an instance of PaymentCustomersList200Response from a dict
payment_customers_list200_response_form_dict = payment_customers_list200_response.from_dict(payment_customers_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


