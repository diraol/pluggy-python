# CreatePaymentCustomerRequestBody

Response with information related to a payment customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Customer type | 
**name** | **str** | Customer name | 
**email** | **str** | Customer email | 
**cpf** | **str** | Customer CPF | [optional] 
**cnpj** | **str** | Customer CNPJ, if type is &#x60;BUSINESS&#x60; | [optional] 

## Example

```python
from openapi_client.models.create_payment_customer_request_body import CreatePaymentCustomerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentCustomerRequestBody from a JSON string
create_payment_customer_request_body_instance = CreatePaymentCustomerRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentCustomerRequestBody.to_json())

# convert the object into a dict
create_payment_customer_request_body_dict = create_payment_customer_request_body_instance.to_dict()
# create an instance of CreatePaymentCustomerRequestBody from a dict
create_payment_customer_request_body_form_dict = create_payment_customer_request_body.from_dict(create_payment_customer_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


