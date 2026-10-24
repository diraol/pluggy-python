# AutomaticPixFirstPayment

Definitions for the first payment. It is considered as the user's enrollment payment for the service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Defines the target settlement date of the first payment. Date format must be YYYY-MM-DD (for example: 2025-06-16). If not provided, the first payment is settled immediately, on the day the user authorizes the consent. The first payment must not be settled on the same day as &#x60;startDate&#x60;: if this field is provided it must be a different date, and if it is omitted the consent cannot be created or authorized on the &#x60;startDate&#x60; itself. Otherwise the request fails with &#x60;AUTOMATIC_PIX_INVALID_FIRST_PAYMENT_DATE&#x60;. | [optional] 
**description** | **str** | Description for the first payment. If not provided, the description will be the same as the description of the payment request | [optional] 
**amount** | **float** | Amount for the first payment. | 

## Example

```python
from pluggy_sdk.models.automatic_pix_first_payment import AutomaticPixFirstPayment

# TODO update the JSON string below
json = "{}"
# create an instance of AutomaticPixFirstPayment from a JSON string
automatic_pix_first_payment_instance = AutomaticPixFirstPayment.from_json(json)
# print the JSON string representation of the object
print(AutomaticPixFirstPayment.to_json())

# convert the object into a dict
automatic_pix_first_payment_dict = automatic_pix_first_payment_instance.to_dict()
# create an instance of AutomaticPixFirstPayment from a dict
automatic_pix_first_payment_from_dict = AutomaticPixFirstPayment.from_dict(automatic_pix_first_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


