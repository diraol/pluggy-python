# AcquirerReceivable

Acquirer Receivable product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier of the acquirer receivable | 
**item_id** | **str** | Primary identifier of the item associated to the acquirer receivable | 
**description** | **str** | Clean description of the acquirer receivable | 
**currency_code** | **str** | Currency ISO code | 
**var_date** | **datetime** | Date when the acquirer receivable was received | 
**gross_amount** | **float** | Acquirer sale gross amount | 
**payment_id** | **str** |  | [optional] 
**settlement_status** | **str** | Status of the payment | [optional] 
**card_flag** | **str** | Flag of the card used | [optional] 
**net_amount** | **float** | Acquirer receivable net amount | [optional] 
**destination_account** | [**AcquirerReceivableDestinationAccount**](AcquirerReceivableDestinationAccount.md) |  | [optional] 
**related_sales** | [**List[AcquirerReceivableRelatedSale]**](AcquirerReceivableRelatedSale.md) | Sales related to the receivable | [optional] 

## Example

```python
from openapi_client.models.acquirer_receivable import AcquirerReceivable

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerReceivable from a JSON string
acquirer_receivable_instance = AcquirerReceivable.from_json(json)
# print the JSON string representation of the object
print(AcquirerReceivable.to_json())

# convert the object into a dict
acquirer_receivable_dict = acquirer_receivable_instance.to_dict()
# create an instance of AcquirerReceivable from a dict
acquirer_receivable_form_dict = acquirer_receivable.from_dict(acquirer_receivable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


