# PaymentRecipientsInstitutionList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[PaymentInstitution]**](PaymentInstitution.md) | List of payment institutions | [optional] 

## Example

```python
from pluggy_sdk.models.payment_recipients_institution_list200_response import PaymentRecipientsInstitutionList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRecipientsInstitutionList200Response from a JSON string
payment_recipients_institution_list200_response_instance = PaymentRecipientsInstitutionList200Response.from_json(json)
# print the JSON string representation of the object
print(PaymentRecipientsInstitutionList200Response.to_json())

# convert the object into a dict
payment_recipients_institution_list200_response_dict = payment_recipients_institution_list200_response_instance.to_dict()
# create an instance of PaymentRecipientsInstitutionList200Response from a dict
payment_recipients_institution_list200_response_form_dict = payment_recipients_institution_list200_response.from_dict(payment_recipients_institution_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


