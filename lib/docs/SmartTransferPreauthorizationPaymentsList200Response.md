# SmartTransferPreauthorizationPaymentsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[SmartTransferPayment]**](SmartTransferPayment.md) | List of payments | [optional] 

## Example

```python
from pluggy_sdk.models.smart_transfer_preauthorization_payments_list200_response import SmartTransferPreauthorizationPaymentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferPreauthorizationPaymentsList200Response from a JSON string
smart_transfer_preauthorization_payments_list200_response_instance = SmartTransferPreauthorizationPaymentsList200Response.from_json(json)
# print the JSON string representation of the object
print(SmartTransferPreauthorizationPaymentsList200Response.to_json())

# convert the object into a dict
smart_transfer_preauthorization_payments_list200_response_dict = smart_transfer_preauthorization_payments_list200_response_instance.to_dict()
# create an instance of SmartTransferPreauthorizationPaymentsList200Response from a dict
smart_transfer_preauthorization_payments_list200_response_from_dict = SmartTransferPreauthorizationPaymentsList200Response.from_dict(smart_transfer_preauthorization_payments_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


