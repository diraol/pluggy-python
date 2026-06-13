# Transaction

Transaction product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier of the transaction | 
**description** | **str** | Clean description of the transaction | 
**description_raw** | **str** | Original transaction description as returned by the institution, before any cleanup or normalization. May be null when not provided by the institution. | [optional] 
**currency_code** | **str** | Currency ISO code | 
**amount** | **float** | Transaction amount | 
**amount_in_account_currency** | **float** | Transaction amount in Account&#39;s Currency. Only present if the transaction is in a different currency than the account&#39;s currency | [optional] 
**var_date** | **datetime** | Date when the transaction was made | 
**type** | **str** | Direction of the movement from the account holder&#39;s perspective. - &#x60;CREDIT&#x60;: money entered the account (deposits, incoming transfers, refunds). - &#x60;DEBIT&#x60;: money left the account (payments, withdrawals, outgoing transfers, credit-card purchases).  Note: for credit-card accounts the convention is inverted at the institution but Pluggy normalizes the value so purchases are always &#x60;DEBIT&#x60; and payments to the card statement are &#x60;CREDIT&#x60;. | [optional] 
**balance** | **float** | Account balance immediately after the transaction was posted. May be null when the institution does not return a running balance. | [optional] 
**provider_code** | **str** | Institution-provided identifier or code for the transaction (e.g. NSU, transaction number on the bank statement). Format varies per institution. | [optional] 
**status** | **str** | Settlement status of the movement. - &#x60;POSTED&#x60;: the transaction is confirmed/settled at the institution. - &#x60;PENDING&#x60;: the transaction is authorized but not yet settled (typical for credit-card purchases not yet included in a closed bill). | [optional] 
**category** | **str** | Category of the transaction (e.g. Restaurants, Education). See the Transaction Categorization section in our guides. | [optional] 
**category_id** | **str** | Id of the transaction category. Can be used to identify the category in the Categories endpoint | [optional] 
**payment_data** | [**PaymentData**](PaymentData.md) |  | [optional] 
**credit_card_metadata** | [**CreditCardMetadata**](CreditCardMetadata.md) |  | [optional] 
**merchant** | [**Merchant**](Merchant.md) |  | [optional] 
**operation_type** | **str** | Type of operation classified by the institution. Only returned for Open Finance connectors. | [optional] 
**operation_type_additional_info** | **str** | Complementary, free-form information about the operation type, as provided by the institution. Varies by institution (a sub-type code or a description). Only returned for Open Finance connectors. | [optional] 
**provider_id** | **str** | Provider&#39;s identifier for the transaction. Only returned for Open Finance connectors. | [optional] 
**account_id** | **UUID** | Identifier of the account this transaction belongs to. | 
**order** | **float** | Sequential position of the transaction within the same day, used to preserve ordering when multiple transactions share the same date. | [optional] 
**created_at** | **datetime** | Date when the transaction was first ingested by Pluggy. | 
**updated_at** | **datetime** | Date of the last update of the transaction data. | 

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


