# PaymentDataBoletoMetadata

Information of the boleto associated with the payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digitable_line** | **str** | Boleto identifier | [optional] 
**barcode** | **str** | Boleto barcode number | [optional] 
**base_amount** | **float** | Boleto original amount without considering penalties / interests / discounts | [optional] 
**interest_amount** | **float** | Boleto interest amount | [optional] 
**penalty_amount** | **float** | Boleto penalty amount | [optional] 
**discount_amount** | **float** | Boleto discount amount | [optional] 

## Example

```python
from pluggy_sdk.models.payment_data_boleto_metadata import PaymentDataBoletoMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDataBoletoMetadata from a JSON string
payment_data_boleto_metadata_instance = PaymentDataBoletoMetadata.from_json(json)
# print the JSON string representation of the object
print(PaymentDataBoletoMetadata.to_json())

# convert the object into a dict
payment_data_boleto_metadata_dict = payment_data_boleto_metadata_instance.to_dict()
# create an instance of PaymentDataBoletoMetadata from a dict
payment_data_boleto_metadata_from_dict = PaymentDataBoletoMetadata.from_dict(payment_data_boleto_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


