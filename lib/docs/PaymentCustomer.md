# PaymentCustomer

Response with information related to a payment customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**type** | [**PaymentCustomerType**](PaymentCustomerType.md) |  | 
**name** | **str** | Customer name | 
**email** | **str** | Customer email | [optional] 
**cpf** | **str** | Customer CPF | [optional] 
**cnpj** | **str** | Customer CNPJ, if type is &#x60;BUSINESS&#x60; | [optional] 
**connector** | [**Connector**](Connector.md) | Default institution to be used in the Pluggy&#39;s payment initiation flow (https://pay.pluggy.ai) by the payer. | [optional] 
**created_at** | **datetime** | Date when the customer was created | 
**updated_at** | **datetime** | Date when the customer was last updated | 

## Example

```python
from pluggy_sdk.models.payment_customer import PaymentCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCustomer from a JSON string
payment_customer_instance = PaymentCustomer.from_json(json)
# print the JSON string representation of the object
print(PaymentCustomer.to_json())

# convert the object into a dict
payment_customer_dict = payment_customer_instance.to_dict()
# create an instance of PaymentCustomer from a dict
payment_customer_from_dict = PaymentCustomer.from_dict(payment_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


