# BoletoPaymentRecipient

Payment recipient inferred from a boleto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Recipient name from the boleto | [optional] 
**tax_number** | **str** | Recipient CPF or CNPJ from the boleto | [optional] 

## Example

```python
from pluggy_sdk.models.boleto_payment_recipient import BoletoPaymentRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of BoletoPaymentRecipient from a JSON string
boleto_payment_recipient_instance = BoletoPaymentRecipient.from_json(json)
# print the JSON string representation of the object
print(BoletoPaymentRecipient.to_json())

# convert the object into a dict
boleto_payment_recipient_dict = boleto_payment_recipient_instance.to_dict()
# create an instance of BoletoPaymentRecipient from a dict
boleto_payment_recipient_from_dict = BoletoPaymentRecipient.from_dict(boleto_payment_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


