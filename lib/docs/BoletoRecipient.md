# BoletoRecipient

Boleto recipient information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** | Recipient CPF or CNPJ | 
**name** | **str** | Recipient name | 

## Example

```python
from pluggy_sdk.models.boleto_recipient import BoletoRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of BoletoRecipient from a JSON string
boleto_recipient_instance = BoletoRecipient.from_json(json)
# print the JSON string representation of the object
print(BoletoRecipient.to_json())

# convert the object into a dict
boleto_recipient_dict = boleto_recipient_instance.to_dict()
# create an instance of BoletoRecipient from a dict
boleto_recipient_from_dict = BoletoRecipient.from_dict(boleto_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


