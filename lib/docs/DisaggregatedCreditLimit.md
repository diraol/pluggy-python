# DisaggregatedCreditLimit

Disaggregated credit card limit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_line_limit_type** | **str** | Limit type (LIMITE_CREDITO_TOTAL or LIMITE_CREDITO_MODALIDADE_OPERACAO) | 
**consolidation_type** | **str** | Indicates if the limit is consolidated or individual | 
**identification_number** | **str** | Identification number of the additional credit card | 
**is_limit_flexible** | **bool** | Indicates if the limit is flexible | 
**used_amount** | **float** | Used amount of the additional credit card | 
**used_amount_currency_code** | **str** | Used amount currency code (for example, BRL) | 
**line_name** | **str** | Name of the line (for example, &#39;Limite de Crédito&#39;) | [optional] 
**line_name_additional_info** | **str** | Additional information about the line name | [optional] 
**limit_amount** | **float** | Limit amount of the additional credit card | [optional] 
**limit_amount_currency_code** | **str** | Limit amount currency code (for example, BRL) | [optional] 
**available_amount** | **float** | Available amount of the additional credit card | [optional] 
**available_amount_currency_code** | **str** | Available amount currency code (for example, BRL) | [optional] 

## Example

```python
from pluggy_sdk.models.disaggregated_credit_limit import DisaggregatedCreditLimit

# TODO update the JSON string below
json = "{}"
# create an instance of DisaggregatedCreditLimit from a JSON string
disaggregated_credit_limit_instance = DisaggregatedCreditLimit.from_json(json)
# print the JSON string representation of the object
print(DisaggregatedCreditLimit.to_json())

# convert the object into a dict
disaggregated_credit_limit_dict = disaggregated_credit_limit_instance.to_dict()
# create an instance of DisaggregatedCreditLimit from a dict
disaggregated_credit_limit_from_dict = DisaggregatedCreditLimit.from_dict(disaggregated_credit_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


