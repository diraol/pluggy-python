# BenefitLoanClient

Client information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Client name | [optional] 
**document** | **str** | Client CPF | [optional] 
**phone** | **str** | Client phone | [optional] 
**addres_street** | **str** | Client email | [optional] 
**address_number** | **str** | Client address number | [optional] 
**address_city** | **str** | Client address city | [optional] 
**address_zip_code** | **str** | Client address zip code | [optional] 
**address_state** | **str** | Client address state | [optional] 

## Example

```python
from pluggy_sdk.models.benefit_loan_client import BenefitLoanClient

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitLoanClient from a JSON string
benefit_loan_client_instance = BenefitLoanClient.from_json(json)
# print the JSON string representation of the object
print(BenefitLoanClient.to_json())

# convert the object into a dict
benefit_loan_client_dict = benefit_loan_client_instance.to_dict()
# create an instance of BenefitLoanClient from a dict
benefit_loan_client_from_dict = BenefitLoanClient.from_dict(benefit_loan_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


