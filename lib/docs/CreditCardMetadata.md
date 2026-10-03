# CreditCardMetadata

Data of a transaction specific to credit card transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installment_number** | **float** | Number of the current installment of the purchase | [optional] 
**total_installments** | **float** | Total number of installments of the purchase | [optional] 
**total_amount** | **float** | Total amount of the purchase. Only available on direct connectors; Open Finance connectors do not return this field | [optional] 
**fee_type** | **str** | Type of fee charged. Present when the operation is a fee (TARIFA) | [optional] 
**fee_type_additional_info** | **str** | Free text describing the fee type when feeType is &#39;OTHER&#39; | [optional] 
**other_credits_type** | **str** | Other type of credit contracted on the card. Present when the operation is a contracted credit operation | [optional] 
**other_credits_additional_info** | **str** | Free text describing the other credit type when otherCreditsType is &#39;OTHER&#39; | [optional] 
**purchase_date** | **datetime** | Original Date of the purchase | [optional] 
**payee_mcc** | **int** | Merchant Category Code of the merchant | [optional] 
**card_number** | **str** | Credit Card Number associated with transaction, can be different from the account if its done by an additional or virtual card. | [optional] 
**bill_id** | **str** | Id of the bill associated to this transaction | [optional] 
**bill_forecast_date** | **str** | Forecasted bill period (formatted as YYYY-MM) in which this transaction is expected to be charged. Unlike billId, it is provided for pending and future transactions too. Only returned for Open Finance connectors | [optional] 
**payment_type** | **str** | How the purchase is charged: &#39;SINGLE&#39; when it is charged in full on one bill, &#39;INSTALLMENT&#39; when it is split into installments. Only returned for Open Finance connectors. Populated from the release of this field onwards, not retroactively: transactions synced before it do not carry the key until they are synced again | [optional] 
**bill_post_date** | **date** | Date (YYYY-MM-DD) the institution posted the transaction to a bill, exactly as the institution reports it. Unlike the transaction &#39;date&#39;, it is never adjusted by Pluggy. null when the transaction is not posted to a bill yet or the institution does not report it. A missing key means the same as null: the field is populated from its release onwards, not retroactively. Only returned for Open Finance connectors | [optional] 
**transaction_date_time** | **datetime** | Date and time of the transaction as reported by the institution. Normalized to a valid ISO-8601 string: some institutions append a zone id suffix (e.g. &#39;2026-04-09T16:43:35.203Z[GMT]&#39;), which Pluggy removes. Absent when the institution sends a placeholder. Only returned for Open Finance connectors. Populated from the release of this field onwards, not retroactively | [optional] 

## Example

```python
from pluggy_sdk.models.credit_card_metadata import CreditCardMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardMetadata from a JSON string
credit_card_metadata_instance = CreditCardMetadata.from_json(json)
# print the JSON string representation of the object
print(CreditCardMetadata.to_json())

# convert the object into a dict
credit_card_metadata_dict = credit_card_metadata_instance.to_dict()
# create an instance of CreditCardMetadata from a dict
credit_card_metadata_from_dict = CreditCardMetadata.from_dict(credit_card_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


