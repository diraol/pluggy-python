# Transaction

Transaction product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier of the transaction | 
**description** | **str** | Clean description of the transaction | 
**currency_code** | **str** | Currency ISO code | 
**amount** | **float** | Transaction amount | 
**amount_in_account_currency** | **float** | Transaction amount in Account&#39;s Currency. Only present if the transaction is in a different currency than the account&#39;s currency | [optional] 
**var_date** | **datetime** | Date when the transaction was made | 
**type** | **str** | Type of the transaction. DEBIT (outflow) or CREDIT (inflow) | [optional] 
**balance** | **float** | Balance after the transaction | [optional] 
**provider_code** | **str** | Institution provided code | [optional] 
**status** | **str** | Status of the movement. POSTED / PENDING | [optional] 
**category** | **str** | Category of the transaction (e.g. Restaurants, Education). See the Transaction Categorization section in our guides. | [optional] 
**category_id** | **str** | Id of the transaction category. Can be used to identify the category in the Categories endpoint | [optional] 
**payment_data** | [**PaymentData**](PaymentData.md) |  | [optional] 
**credit_card_metadata** | [**CreditCardMetadata**](CreditCardMetadata.md) |  | [optional] 
**merchant** | [**Merchant**](Merchant.md) |  | [optional] 
**operation_type** | **str** | Type of operation classified by the institution. | [optional] 

## Example

```python
from pluggy_sdk.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


