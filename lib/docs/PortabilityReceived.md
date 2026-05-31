# PortabilityReceived

Salary portability received by the institution from a previous paycheck bank (banco-folha). Approved requests only — a portability is never explicitly closed, so an entry doesn't guarantee an active link with the listed paycheck bank

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employer_name** | **str** | Employer name as received in the portability message. When the employer is a legal entity, this is the company name | 
**employer_document** | **str** | Employer document (CPF or CNPJ) as received in the portability message | 
**paycheck_bank_detainer_cnpj** | **str** | CNPJ of the bank that holds the paycheck account (banco-folha) as received in the portability message | 
**paycheck_bank_detainer_ispb** | **str** | ISPB of the bank that holds the paycheck account as received in the portability message | 
**portability_approval_date** | **datetime** | Date the portability was approved | 

## Example

```python
from pluggy_sdk.models.portability_received import PortabilityReceived

# TODO update the JSON string below
json = "{}"
# create an instance of PortabilityReceived from a JSON string
portability_received_instance = PortabilityReceived.from_json(json)
# print the JSON string representation of the object
print(PortabilityReceived.to_json())

# convert the object into a dict
portability_received_dict = portability_received_instance.to_dict()
# create an instance of PortabilityReceived from a dict
portability_received_from_dict = PortabilityReceived.from_dict(portability_received_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


