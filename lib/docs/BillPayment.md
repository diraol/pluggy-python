# BillPayment

Response with information related to a credit card bill payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**value_type** | **str** | Classifies the payment value type | 
**payment_date** | **datetime** | Date when the payment was made | 
**payment_mode** | **str** | Payment mode used | [optional] 
**amount** | **float** | Payment amount | 
**currency_code** | **str** | Code referencing the currency of the payment | 

## Example

```python
from pluggy_sdk.models.bill_payment import BillPayment

# TODO update the JSON string below
json = "{}"
# create an instance of BillPayment from a JSON string
bill_payment_instance = BillPayment.from_json(json)
# print the JSON string representation of the object
print(BillPayment.to_json())

# convert the object into a dict
bill_payment_dict = bill_payment_instance.to_dict()
# create an instance of BillPayment from a dict
bill_payment_from_dict = BillPayment.from_dict(bill_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


