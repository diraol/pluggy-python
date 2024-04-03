# CreditCardMetadata

Data of a transaction specific to credit card transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installment_number** | **float** | Number of the current installment of the purchase | [optional] 
**total_installments** | **float** | Total number of installments of the purchase | [optional] 
**total_amount** | **float** | Total amount of the purchase | [optional] 
**purchase_date** | **datetime** | Original Date of the purchase | [optional] 
**payee_mcc** | **str** | Merchant Category Code of the merchant | [optional] 
**card_number** | **str** | Credit Card Number associated with transaction, can be different from the account if its done by an additional or virtual card. | [optional] 
**bill_id** | **str** | Id of the bill associated to this transaction | [optional] 

## Example

```python
from openapi_client.models.credit_card_metadata import CreditCardMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardMetadata from a JSON string
credit_card_metadata_instance = CreditCardMetadata.from_json(json)
# print the JSON string representation of the object
print(CreditCardMetadata.to_json())

# convert the object into a dict
credit_card_metadata_dict = credit_card_metadata_instance.to_dict()
# create an instance of CreditCardMetadata from a dict
credit_card_metadata_form_dict = credit_card_metadata.from_dict(credit_card_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


