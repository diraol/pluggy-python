# AcquirerReceivableDestinationAccount

Acquirer receivable destination account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiving_bank** | **str** | Name of the receiving bank | 
**agency** | **str** | Agency of the receiving account | 
**account** | **str** | Number of the receiving account | 

## Example

```python
from pluggy_sdk.models.acquirer_receivable_destination_account import AcquirerReceivableDestinationAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerReceivableDestinationAccount from a JSON string
acquirer_receivable_destination_account_instance = AcquirerReceivableDestinationAccount.from_json(json)
# print the JSON string representation of the object
print(AcquirerReceivableDestinationAccount.to_json())

# convert the object into a dict
acquirer_receivable_destination_account_dict = acquirer_receivable_destination_account_instance.to_dict()
# create an instance of AcquirerReceivableDestinationAccount from a dict
acquirer_receivable_destination_account_from_dict = AcquirerReceivableDestinationAccount.from_dict(acquirer_receivable_destination_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


