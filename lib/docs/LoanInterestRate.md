# LoanInterestRate

Object that brings the set of information necessary to demonstrate the composition of the remunerative interest rates of the Credit Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_type** | **str** | Tax type | [optional] 
**interest_rate_type** | **str** | Interest rate type | [optional] 
**tax_periodicity** | **str** | Tax periodicity | [optional] 
**calculation** | **str** | Calculation basis | [optional] 
**referential_rate_indexer_type** | **str** | Types of benchmark rates or indexers (https://openbanking-brasil.github.io/openapi/swagger-apis/loans/?urls.primaryName&#x3D;2.0.1#model-EnumContractReferentialRateIndexerType) | [optional] 
**referential_rate_indexer_sub_type** | **str** | Subtypes of benchmark rates or indexers (https://openbanking-brasil.github.io/openapi/swagger-apis/loans/?urls.primaryName&#x3D;2.0.1#model-EnumContractReferentialRateIndexerSubType) | [optional] 
**referential_rate_indexer_additional_info** | **str** | Free field to complement the information regarding the Type of reference rate or indexer | [optional] 
**pre_fixed_rate** | **float** | Pre-fixed rate applied under the credit modality contract. 1 &#x3D; 100% | [optional] 
**post_fixed_rate** | **float** | Post-fixed rate applied under the credit modality contract. 1 &#x3D; 100% | [optional] 
**additional_info** | **str** | Text with additional information on the composition of agreed interest rates | [optional] 

## Example

```python
from openapi_client.models.loan_interest_rate import LoanInterestRate

# TODO update the JSON string below
json = "{}"
# create an instance of LoanInterestRate from a JSON string
loan_interest_rate_instance = LoanInterestRate.from_json(json)
# print the JSON string representation of the object
print(LoanInterestRate.to_json())

# convert the object into a dict
loan_interest_rate_dict = loan_interest_rate_instance.to_dict()
# create an instance of LoanInterestRate from a dict
loan_interest_rate_form_dict = loan_interest_rate.from_dict(loan_interest_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


