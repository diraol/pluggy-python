# Merchant

Merchant extracted from the transaction data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Merchants name | [optional] 
**business_name** | **str** | Merchant legal business name | [optional] 
**cnpj** | **str** | Document number related to the merchant | [optional] 
**cnae** | **str** | Economic activity classification number related to the merchant | [optional] 
**category** | **str** | Merchant associated category | [optional] 

## Example

```python
from pluggy_sdk.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print(Merchant.to_json())

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_from_dict = Merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


