# Bill

Response with information related to a credit card bill

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**due_date** | **datetime** | Due date of the bill, displayed for payment by the customer | 
**total_amount** | **float** | Total bill amount | 
**total_amount_currency_code** | **str** | Code referencing the currency of the bill | 
**minimum_payment_amount** | **float** | Minimum payment amount of the bill | [optional] 
**allows_installments** | **bool** | Indicates whether the bill allows installment payments (true) or not (false) | [optional] 
**finance_charges** | [**List[BillFinanceCharge]**](BillFinanceCharge.md) | List of charges associated to the bill | 

## Example

```python
from openapi_client.models.bill import Bill

# TODO update the JSON string below
json = "{}"
# create an instance of Bill from a JSON string
bill_instance = Bill.from_json(json)
# print the JSON string representation of the object
print(Bill.to_json())

# convert the object into a dict
bill_dict = bill_instance.to_dict()
# create an instance of Bill from a dict
bill_form_dict = bill.from_dict(bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


