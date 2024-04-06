# CreditData

Credit account additional fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Card level (Black, Signature) | [optional] 
**brand** | **str** | Card Brand (Visa, Mastercard, Elo) | [optional] 
**balance_close_date** | **datetime** | Date when the balance was closed | [optional] 
**balance_due_date** | **datetime** | Date when the balance is dued | [optional] 
**available_credit_limit** | **float** | Credit limit available to spent | [optional] 
**balance_foreign_currency** | **float** | Balance in USD | [optional] 
**minimum_payment** | **float** | Minimum payment due | [optional] 
**credit_limit** | **float** | Maximum amount that can be spent | [optional] 
**status** | **str** | Credit card status | [optional] 
**holder_type** | **str** | Credit card holder type | [optional] 

## Example

```python
from pluggy_sdk.models.credit_data import CreditData

# TODO update the JSON string below
json = "{}"
# create an instance of CreditData from a JSON string
credit_data_instance = CreditData.from_json(json)
# print the JSON string representation of the object
print(CreditData.to_json())

# convert the object into a dict
credit_data_dict = credit_data_instance.to_dict()
# create an instance of CreditData from a dict
credit_data_form_dict = credit_data.from_dict(credit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


