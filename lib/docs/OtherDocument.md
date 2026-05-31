# OtherDocument

Other identification document held by the natural person. Brazilian acronyms are kept verbatim; OTHER covers any other type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Document type | 
**type_additional_info** | **str** | Free-text complement. Populated when type is OTHER | [optional] 
**number** | **str** | Document number | 
**check_digit** | **str** | Check digit of the document, if it has one | [optional] 
**additional_info** | **str** | Free-text complement, used to record the issuing authority (e.g. &#39;SSP/SP&#39;) when relevant | [optional] 
**expiration_date** | **datetime** | Expiration date of the document | [optional] 

## Example

```python
from pluggy_sdk.models.other_document import OtherDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OtherDocument from a JSON string
other_document_instance = OtherDocument.from_json(json)
# print the JSON string representation of the object
print(OtherDocument.to_json())

# convert the object into a dict
other_document_dict = other_document_instance.to_dict()
# create an instance of OtherDocument from a dict
other_document_from_dict = OtherDocument.from_dict(other_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


