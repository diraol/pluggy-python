# PaymentDataParticipant

Participant of the payment data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_number** | [**Document**](Document.md) |  | [optional] 
**name** | **str** | Fullname of the participant | [optional] 
**account_number** | **str** | Account number on the branch | [optional] 
**branch_number** | **str** | Agency number | [optional] 
**routing_number** | **str** | COMPE Bank number | [optional] 
**routing_number_ispb** | **str** | ISPB Bank number | [optional] 

## Example

```python
from pluggy_sdk.models.payment_data_participant import PaymentDataParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDataParticipant from a JSON string
payment_data_participant_instance = PaymentDataParticipant.from_json(json)
# print the JSON string representation of the object
print(PaymentDataParticipant.to_json())

# convert the object into a dict
payment_data_participant_dict = payment_data_participant_instance.to_dict()
# create an instance of PaymentDataParticipant from a dict
payment_data_participant_form_dict = payment_data_participant.from_dict(payment_data_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


