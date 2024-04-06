# LoanWarranty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Code referencing the currency of the warranty | [optional] 
**type** | **str** | Denomination / Identification of the type of warranty that guarantees the Type of Credit Operation contracted (https://openbanking-brasil.github.io/openapi/swagger-apis/loans/?urls.primaryName&#x3D;2.0.1#model-EnumWarrantyType) | [optional] 
**subtype** | **str** | Denomination / Identification of the subtype of warranty that guarantees the Type of Credit Operation contracted (https://openbanking-brasil.github.io/openapi/swagger-apis/loans/?urls.primaryName&#x3D;2.0.1#model-EnumWarrantySubType) | [optional] 
**amount** | **float** | Warranty original value | [optional] 

## Example

```python
from pluggy_sdk.models.loan_warranty import LoanWarranty

# TODO update the JSON string below
json = "{}"
# create an instance of LoanWarranty from a JSON string
loan_warranty_instance = LoanWarranty.from_json(json)
# print the JSON string representation of the object
print(LoanWarranty.to_json())

# convert the object into a dict
loan_warranty_dict = loan_warranty_instance.to_dict()
# create an instance of LoanWarranty from a dict
loan_warranty_form_dict = loan_warranty.from_dict(loan_warranty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


