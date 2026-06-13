# CreateOrUpdatePaymentCustomer

Body to update a payment customer. All fields are optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PaymentCustomerType**](PaymentCustomerType.md) |  | [optional] 
**name** | **str** | Customer name | [optional] 
**email** | **str** | Customer email | [optional] 
**cpf** | **str** | Customer CPF | [optional] 
**cnpj** | **str** | Customer CNPJ, if type is &#x60;BUSINESS&#x60; | [optional] 

## Example

```python
from pluggy_sdk.models.create_or_update_payment_customer import CreateOrUpdatePaymentCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdatePaymentCustomer from a JSON string
create_or_update_payment_customer_instance = CreateOrUpdatePaymentCustomer.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdatePaymentCustomer.to_json())

# convert the object into a dict
create_or_update_payment_customer_dict = create_or_update_payment_customer_instance.to_dict()
# create an instance of CreateOrUpdatePaymentCustomer from a dict
create_or_update_payment_customer_from_dict = CreateOrUpdatePaymentCustomer.from_dict(create_or_update_payment_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


