# PaymentData

Payment or Transfer participant's data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer** | [**PaymentDataParticipant**](PaymentDataParticipant.md) |  | [optional] 
**receiver** | [**PaymentDataParticipant**](PaymentDataParticipant.md) |  | [optional] 
**reason** | **str** | User&#39;s motive submitted while making the transfer | [optional] 
**reference_number** | **str** | Reference number for the transfer/payment | [optional] 
**receiver_reference_id** | **str** | String submitted by the receiver associated with the payment when generating the payment request. | [optional] 
**payment_method** | **str** | Type of transfer. TED, DOC, PIX or TEV | [optional] 

## Example

```python
from pluggy_sdk.models.payment_data import PaymentData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentData from a JSON string
payment_data_instance = PaymentData.from_json(json)
# print the JSON string representation of the object
print(PaymentData.to_json())

# convert the object into a dict
payment_data_dict = payment_data_instance.to_dict()
# create an instance of PaymentData from a dict
payment_data_form_dict = payment_data.from_dict(payment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


