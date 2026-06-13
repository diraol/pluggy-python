# IssuedBoleto

Response with information related to an issued boleto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**amount** | **float** | Boleto amount | 
**status** | **str** | Current status of the boleto. - &#x60;OPEN&#x60;: the boleto has been issued and is awaiting payment. - &#x60;PAID&#x60;: the boleto has been paid (see &#x60;paidAt&#x60;, &#x60;amountPaid&#x60;, &#x60;paymentOrigin&#x60;). - &#x60;OVERDUE&#x60;: the due date has passed and the boleto has not been paid. - &#x60;CANCELLED&#x60;: the boleto was canceled by the issuer. - &#x60;PROTESTED&#x60;: the boleto was sent to a protesto/credit-bureau process. | 
**seu_numero** | **str** | Your identifier for this boleto | 
**due_date** | **datetime** | Due date of the boleto | 
**payer** | [**IssuedBoletoPayer**](IssuedBoletoPayer.md) |  | 
**pix_qr** | **str** | PIX QR code for payment | [optional] 
**digitable_line** | **str** | Boleto digitable line | 
**nosso_numero** | **str** | Bank&#39;s internal identifier for the boleto | [optional] 
**barcode** | **str** | Boleto barcode | 
**boleto_connection_id** | **UUID** | ID of the boleto connection used to create this boleto | 
**created_at** | **datetime** | Date when the boleto was created | 
**amount_paid** | **float** | Amount that was paid for this boleto | [optional] 
**payment_origin** | **str** | Origin of the payment when the boleto is paid | [optional] 
**fine** | [**IssuedBoletoFine**](IssuedBoletoFine.md) |  | [optional] 
**interest** | [**IssuedBoletoInterest**](IssuedBoletoInterest.md) |  | [optional] 
**paid_at** | **datetime** | Date when the boleto was paid | [optional] 

## Example

```python
from pluggy_sdk.models.issued_boleto import IssuedBoleto

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedBoleto from a JSON string
issued_boleto_instance = IssuedBoleto.from_json(json)
# print the JSON string representation of the object
print(IssuedBoleto.to_json())

# convert the object into a dict
issued_boleto_dict = issued_boleto_instance.to_dict()
# create an instance of IssuedBoleto from a dict
issued_boleto_from_dict = IssuedBoleto.from_dict(issued_boleto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


