# AutomaticPixPaymentDetail

Automatic PIX payment detail with additional fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Payment primary identifier | 
**status** | **str** | Payment status | 
**amount** | **float** | Payment amount | 
**description** | **str** | Payment description | [optional] 
**var_date** | **date** | Payment scheduled date | 
**end_to_end_id** | **str** | Payment end to end identifier | [optional] 
**error_detail** | [**AutomaticPixPaymentErrorDetail**](AutomaticPixPaymentErrorDetail.md) |  | [optional] 
**client_payment_id** | **str** | External identifier for the payment | [optional] 
**recipient_id** | **UUID** | Payment recipient identifier | 
**is_first_payment** | **bool** | Indicates if this is the first payment | [optional] 
**attempts** | [**List[AutomaticPixPaymentAttempt]**](AutomaticPixPaymentAttempt.md) |  | [optional] 
**scheduled_status_reached** | **bool** | Indicates whether the payment reached the scheduled status in the last attempt. Useful to determine if a retry can be executed. | 

## Example

```python
from pluggy_sdk.models.automatic_pix_payment_detail import AutomaticPixPaymentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AutomaticPixPaymentDetail from a JSON string
automatic_pix_payment_detail_instance = AutomaticPixPaymentDetail.from_json(json)
# print the JSON string representation of the object
print(AutomaticPixPaymentDetail.to_json())

# convert the object into a dict
automatic_pix_payment_detail_dict = automatic_pix_payment_detail_instance.to_dict()
# create an instance of AutomaticPixPaymentDetail from a dict
automatic_pix_payment_detail_from_dict = AutomaticPixPaymentDetail.from_dict(automatic_pix_payment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


