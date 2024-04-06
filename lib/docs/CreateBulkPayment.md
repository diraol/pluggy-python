# CreateBulkPayment

Request with information to create a bulk payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_request_ids** | **List[str]** | List of payment request identifiers to be associated with the bulk payment | 
**callback_urls** | [**PaymentRequestCallbackUrls**](PaymentRequestCallbackUrls.md) |  | [optional] 
**smart_account_id** | **str** | Smart account identifier associated with the bulk payment | 

## Example

```python
from pluggy_sdk.models.create_bulk_payment import CreateBulkPayment

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkPayment from a JSON string
create_bulk_payment_instance = CreateBulkPayment.from_json(json)
# print the JSON string representation of the object
print(CreateBulkPayment.to_json())

# convert the object into a dict
create_bulk_payment_dict = create_bulk_payment_instance.to_dict()
# create an instance of CreateBulkPayment from a dict
create_bulk_payment_form_dict = create_bulk_payment.from_dict(create_bulk_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


