# SmartTransferPaymentErrorDetail

Error detail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code.  - INFRASTRUCTURE_FAILURE: Indicates a failure in the infrastructure of the institution holding the information or resources. - PAYMENT_DIFFERENT_FROM_CONSENT: Payment data differs from consent data. - UNKNOWN_ERROR: Unknown error. - INVALID_PAYMENT_DETAIL: The payment detail is invalid. - PAYMENT_REJECTED_BY_HOLDER: The payment was rejected by the account holder. - PAYMENT_REJECTED_BY_SPI: The payment was rejected by the SPI. | [optional] 
**description** | **str** | Error description | [optional] 
**detail** | **str** | Error detail | [optional] 

## Example

```python
from pluggy_sdk.models.smart_transfer_payment_error_detail import SmartTransferPaymentErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPaymentErrorDetail from a JSON string
smart_transfer_payment_error_detail_instance = SmartTransferPaymentErrorDetail.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPaymentErrorDetail.to_json())

# convert the object into a dict
smart_transfer_payment_error_detail_dict = smart_transfer_payment_error_detail_instance.to_dict()
# create an instance of SmartTransferPaymentErrorDetail from a dict
smart_transfer_payment_error_detail_from_dict = SmartTransferPaymentErrorDetail.from_dict(smart_transfer_payment_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


