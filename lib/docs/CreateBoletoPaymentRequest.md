# CreateBoletoPaymentRequest

Request with information to create a boleto payment request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Payment description | [optional] 
**boleto_digitable_line** | **str** | Boleto digitable line | 
**callback_urls** | [**PaymentRequestCallbackUrls**](PaymentRequestCallbackUrls.md) |  | [optional] 
**customer_id** | **str** | Customer identifier associated to the payment | [optional] 

## Example

```python
from pluggy_sdk.models.create_boleto_payment_request import CreateBoletoPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBoletoPaymentRequest from a JSON string
create_boleto_payment_request_instance = CreateBoletoPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBoletoPaymentRequest.to_json())

# convert the object into a dict
create_boleto_payment_request_dict = create_boleto_payment_request_instance.to_dict()
# create an instance of CreateBoletoPaymentRequest from a dict
create_boleto_payment_request_from_dict = CreateBoletoPaymentRequest.from_dict(create_boleto_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


