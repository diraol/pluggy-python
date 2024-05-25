# PaymentReceipt

Response with information related to a payment receipt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**payment_request_id** | **str** | Payment request identifier | 
**expires_at** | **datetime** | Date when the payment receipt expires | 
**receipt_url** | **str** | URL to download the payment receipt | 
**creditor** | [**PaymentReceiptPerson**](PaymentReceiptPerson.md) | Creditor bank account information | 
**debtor** | [**PaymentReceiptPerson**](PaymentReceiptPerson.md) | Debtor bank account information | 
**amount** | **float** | Payment amount | 
**description** | **str** | Payment description | [optional] 
**reference_id** | **str** | Payment reference identifier | 
**var_date** | **datetime** | Date when the payment was made | [optional] 
**boleto** | [**Boleto**](Boleto.md) |  | [optional] 

## Example

```python
from pluggy_sdk.models.payment_receipt import PaymentReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReceipt from a JSON string
payment_receipt_instance = PaymentReceipt.from_json(json)
# print the JSON string representation of the object
print(PaymentReceipt.to_json())

# convert the object into a dict
payment_receipt_dict = payment_receipt_instance.to_dict()
# create an instance of PaymentReceipt from a dict
payment_receipt_from_dict = PaymentReceipt.from_dict(payment_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


