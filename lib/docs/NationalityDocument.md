# NationalityDocument

Supporting document for a non-Brazilian nationality

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Document type (free text). Required when the nationality is not Brazilian | 
**number** | **str** | Document number. Required when the nationality is not Brazilian | 
**country** | **str** | Country name | [optional] 
**issue_date** | **datetime** | Issue date of the document | [optional] 
**expiration_date** | **datetime** | Expiration date of the document | [optional] 
**additional_info** | **str** | Free-text complement | [optional] 

## Example

```python
from pluggy_sdk.models.nationality_document import NationalityDocument

# TODO update the JSON string below
json = "{}"
# create an instance of NationalityDocument from a JSON string
nationality_document_instance = NationalityDocument.from_json(json)
# print the JSON string representation of the object
print(NationalityDocument.to_json())

# convert the object into a dict
nationality_document_dict = nationality_document_instance.to_dict()
# create an instance of NationalityDocument from a dict
nationality_document_from_dict = NationalityDocument.from_dict(nationality_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


