# CreateAutomaticPixPaymentRequest

Automatic PIX data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_amount** | **float** | Fixed charge amount; if filled in, it represents consent for payments of fixed amounts, not subject to change during the validity of the consent. If it&#39;s sent, minimumVariableAmount and maximumVariableAmount cannot be provided. | [optional] 
**minimum_variable_amount** | **float** | Minimum amount allowed per charge; if filled in, it represents consent for payments of variable amounts. If it&#39;s sent, fixedAmount cannot be provided. | [optional] 
**maximum_variable_amount** | **float** | Maximum amount allowed per charge; if filled in, it represents consent for payments of variable amounts. If it&#39;s sent, fixedAmount cannot be provided. | [optional] 
**description** | **str** | Description for the automatic pix authorization | [optional] 
**start_date** | **datetime** | Represents the expected date for the first occurrence of a payment associated with the recurrence. Date format must be YYYY-MM-DD (for example: 2025-06-16) | 
**expires_at** | **datetime** | Expiration date for the automatic pix authorization. The date must be in UTC and the format must follow the following pattern: YYYY-MM-DDTHH:MM:SSZ (for example: 2025-06-16T03:00:00Z). | [optional] 
**is_retry_accepted** | **bool** | Indicates whether the receiving customer is allowed to make payment attempts, according to the rules established in the Pix arrangement. | [optional] 
**first_payment** | [**AutomaticPixFirstPayment**](AutomaticPixFirstPayment.md) |  | [optional] 
**interval** | **str** | Defines the permitted frequency for carrying out transactions. | 
**callback_urls** | [**PaymentRequestCallbackUrls**](PaymentRequestCallbackUrls.md) |  | [optional] 
**recipient_id** | **str** | Primary identifier of the payment recipient | 
**client_payment_id** | **str** | Client payment identifier | [optional] 
**customer_id** | **str** | Primary identifier of the customer | [optional] 

## Example

```python
from pluggy_sdk.models.create_automatic_pix_payment_request import CreateAutomaticPixPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutomaticPixPaymentRequest from a JSON string
create_automatic_pix_payment_request_instance = CreateAutomaticPixPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAutomaticPixPaymentRequest.to_json())

# convert the object into a dict
create_automatic_pix_payment_request_dict = create_automatic_pix_payment_request_instance.to_dict()
# create an instance of CreateAutomaticPixPaymentRequest from a dict
create_automatic_pix_payment_request_from_dict = CreateAutomaticPixPaymentRequest.from_dict(create_automatic_pix_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


