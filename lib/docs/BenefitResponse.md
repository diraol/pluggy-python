# BenefitResponse

Response with information related to a benefit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**item_id** | **str** | Identifier of the item linked to the loan | 
**beneficiary_name** | **str** | Beneficiary name | 
**available_margin_value** | **float** | Available margin value | [optional] 
**margin_base_value** | **float** | Base margin value | [optional] 
**payroll_deductible_available_margin_value** | **float** | Payroll deductible available margin value | [optional] 
**used_margin_value** | **float** | Used margin value | [optional] 
**reserved_margin_value** | **float** | Reserved margin value | [optional] 
**paying_institution** | [**BenefitResponsePayingInstitution**](BenefitResponsePayingInstitution.md) |  | [optional] 
**payroll_loans** | [**List[PayrollLoan]**](PayrollLoan.md) | List of payroll loans | [optional] 

## Example

```python
from pluggy_sdk.models.benefit_response import BenefitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitResponse from a JSON string
benefit_response_instance = BenefitResponse.from_json(json)
# print the JSON string representation of the object
print(BenefitResponse.to_json())

# convert the object into a dict
benefit_response_dict = benefit_response_instance.to_dict()
# create an instance of BenefitResponse from a dict
benefit_response_from_dict = BenefitResponse.from_dict(benefit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


