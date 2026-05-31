# MerchantsGetByCnpj200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found_merchants** | [**List[Merchant]**](Merchant.md) | List of merchants found for the provided CNPJs | 
**not_found_merchants** | **List[str]** | List of valid CNPJs that were not found in the merchant database | 
**invalid_cnpjs** | **List[str]** | List of invalid CNPJ values provided | 

## Example

```python
from pluggy_sdk.models.merchants_get_by_cnpj200_response import MerchantsGetByCnpj200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantsGetByCnpj200Response from a JSON string
merchants_get_by_cnpj200_response_instance = MerchantsGetByCnpj200Response.from_json(json)
# print the JSON string representation of the object
print(MerchantsGetByCnpj200Response.to_json())

# convert the object into a dict
merchants_get_by_cnpj200_response_dict = merchants_get_by_cnpj200_response_instance.to_dict()
# create an instance of MerchantsGetByCnpj200Response from a dict
merchants_get_by_cnpj200_response_from_dict = MerchantsGetByCnpj200Response.from_dict(merchants_get_by_cnpj200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


