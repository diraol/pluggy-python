# PaymentIntentsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[PaymentIntent]**](PaymentIntent.md) | List of payment intents | [optional] 

## Example

```python
from openapi_client.models.payment_intents_list200_response import PaymentIntentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentsList200Response from a JSON string
payment_intents_list200_response_instance = PaymentIntentsList200Response.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentsList200Response.to_json())

# convert the object into a dict
payment_intents_list200_response_dict = payment_intents_list200_response_instance.to_dict()
# create an instance of PaymentIntentsList200Response from a dict
payment_intents_list200_response_form_dict = payment_intents_list200_response.from_dict(payment_intents_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


