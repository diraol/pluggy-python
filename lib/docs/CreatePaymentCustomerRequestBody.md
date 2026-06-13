# CreatePaymentCustomerRequestBody

Body to create a payment customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PaymentCustomerType**](PaymentCustomerType.md) |  | 
**name** | **str** | Customer name | 
**email** | **str** | Customer email | [optional] 
**cpf** | **str** | Customer CPF. Required when &#x60;type&#x3D;INDIVIDUAL&#x60;. | [optional] 
**cnpj** | **str** | Customer CNPJ. Required when &#x60;type&#x3D;BUSINESS&#x60;. | [optional] 
**connector_id** | **float** | Default connector id to be used in the Pluggy&#39;s payment initiation flow (https://pay.pluggy.ai) by the payer. | [optional] 

## Example

```python
from pluggy_sdk.models.create_payment_customer_request_body import CreatePaymentCustomerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentCustomerRequestBody from a JSON string
create_payment_customer_request_body_instance = CreatePaymentCustomerRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentCustomerRequestBody.to_json())

# convert the object into a dict
create_payment_customer_request_body_dict = create_payment_customer_request_body_instance.to_dict()
# create an instance of CreatePaymentCustomerRequestBody from a dict
create_payment_customer_request_body_from_dict = CreatePaymentCustomerRequestBody.from_dict(create_payment_customer_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


