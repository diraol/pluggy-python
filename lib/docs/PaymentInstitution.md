# PaymentInstitution

Response with information related to a payment institution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**name** | **str** | Payment institution name | 
**trade_name** | **str** | Payment institution trade name | 
**ispb** | **str** | Payment institution ISPB | 
**compe** | **str** | Payment institution COMPE | [optional] 
**created_at** | **datetime** | Date when the payment institution was created | 
**updated_at** | **datetime** | Date when the payment institution was updated | 

## Example

```python
from openapi_client.models.payment_institution import PaymentInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstitution from a JSON string
payment_institution_instance = PaymentInstitution.from_json(json)
# print the JSON string representation of the object
print(PaymentInstitution.to_json())

# convert the object into a dict
payment_institution_dict = payment_institution_instance.to_dict()
# create an instance of PaymentInstitution from a dict
payment_institution_form_dict = payment_institution.from_dict(payment_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


