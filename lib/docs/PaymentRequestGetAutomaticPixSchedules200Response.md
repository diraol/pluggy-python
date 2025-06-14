# PaymentRequestGetAutomaticPixSchedules200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[AutomaticPixPayment]**](AutomaticPixPayment.md) | List of automatic PIX payments | [optional] 

## Example

```python
from pluggy_sdk.models.payment_request_get_automatic_pix_schedules200_response import PaymentRequestGetAutomaticPixSchedules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestGetAutomaticPixSchedules200Response from a JSON string
payment_request_get_automatic_pix_schedules200_response_instance = PaymentRequestGetAutomaticPixSchedules200Response.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestGetAutomaticPixSchedules200Response.to_json())

# convert the object into a dict
payment_request_get_automatic_pix_schedules200_response_dict = payment_request_get_automatic_pix_schedules200_response_instance.to_dict()
# create an instance of PaymentRequestGetAutomaticPixSchedules200Response from a dict
payment_request_get_automatic_pix_schedules200_response_from_dict = PaymentRequestGetAutomaticPixSchedules200Response.from_dict(payment_request_get_automatic_pix_schedules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


