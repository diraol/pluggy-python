# BusinessOtherDocument

Additional document for businesses headquartered abroad and not required to register a CNPJ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the document (e.g. &#39;EIN&#39;) | 
**number** | **str** | Document number | 
**country** | **str** | Issuing country in alpha3 ISO-3166 format | 
**expiration_date** | **datetime** | Expiration date of the document | [optional] 

## Example

```python
from pluggy_sdk.models.business_other_document import BusinessOtherDocument

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessOtherDocument from a JSON string
business_other_document_instance = BusinessOtherDocument.from_json(json)
# print the JSON string representation of the object
print(BusinessOtherDocument.to_json())

# convert the object into a dict
business_other_document_dict = business_other_document_instance.to_dict()
# create an instance of BusinessOtherDocument from a dict
business_other_document_from_dict = BusinessOtherDocument.from_dict(business_other_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


