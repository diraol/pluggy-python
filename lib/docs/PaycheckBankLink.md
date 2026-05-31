# PaycheckBankLink

Paycheck-bank (banco-folha) link to an employer, active or formerly active. Old employers may not have closed the link, so an entry doesn't guarantee the listed employer is the current one

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employer_name** | **str** | Employer name as registered when the paycheck account was opened. When the employer is a legal entity, this is the company name | 
**employer_document** | **str** | Employer document (CPF or CNPJ) as registered when the paycheck account was opened | 
**paycheck_bank_cnpj** | **str** | CNPJ of the institution contracted to provide the paycheck service (banco-folha) | 
**paycheck_bank_ispb** | **str** | ISPB of the institution contracted to provide the paycheck service | 
**account_opening_date** | **datetime** | Date the paycheck account was opened | 

## Example

```python
from pluggy_sdk.models.paycheck_bank_link import PaycheckBankLink

# TODO update the JSON string below
json = "{}"
# create an instance of PaycheckBankLink from a JSON string
paycheck_bank_link_instance = PaycheckBankLink.from_json(json)
# print the JSON string representation of the object
print(PaycheckBankLink.to_json())

# convert the object into a dict
paycheck_bank_link_dict = paycheck_bank_link_instance.to_dict()
# create an instance of PaycheckBankLink from a dict
paycheck_bank_link_from_dict = PaycheckBankLink.from_dict(paycheck_bank_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


