# ScrResponse

Bacen's SCR response, forwarded exactly as the Banco Central returns it — field names, codes and all. Nothing is renamed or normalised, so a value read here is the same value an institution reads at the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dtb_consult** | **str** | The base dates consulted | 
**cd_cli** | **str** | The consulted document: the CPF for an individual, or the 8-digit CNPJ root for a company | 
**tp_cli** | **str** | Type of client: \&quot;1\&quot; for an individual, \&quot;2\&quot; for a legal entity | 
**ls_dtb** | [**List[ScrDatabase]**](ScrDatabase.md) | One entry per consulted base date. A base date with no data for the client is still listed, with no operations | [optional] 
**lista_de_mensagens_de_validacao** | [**List[ScrValidationMessage]**](ScrValidationMessage.md) | Validation messages raised by Bacen for this request | [optional] 

## Example

```python
from pluggy_sdk.models.scr_response import ScrResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScrResponse from a JSON string
scr_response_instance = ScrResponse.from_json(json)
# print the JSON string representation of the object
print(ScrResponse.to_json())

# convert the object into a dict
scr_response_dict = scr_response_instance.to_dict()
# create an instance of ScrResponse from a dict
scr_response_from_dict = ScrResponse.from_dict(scr_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


