# PayrollLoanClient

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
from pluggy_sdk.models.payroll_loan_client import PayrollLoanClient

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollLoanClient from a JSON string
payroll_loan_client_instance = PayrollLoanClient.from_json(json)
# print the JSON string representation of the object
print(PayrollLoanClient.to_json())

# convert the object into a dict
payroll_loan_client_dict = payroll_loan_client_instance.to_dict()
# create an instance of PayrollLoanClient from a dict
payroll_loan_client_from_dict = PayrollLoanClient.from_dict(payroll_loan_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


