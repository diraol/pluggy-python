# ScrDatabase

One consulted base date, and what the SCR holds for the client in it

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dtb** | **float** | The base date, as YYYYMM. Numeric, not a string | [optional] 
**msg** | **str** | Bacen&#39;s message for this base date, when it has one — for example that the base date is not available for consultation | [optional] 
**doc_proc** | **str** | Percentage of the expected 3040 documents already incorporated by Bacen for this base date. A low value means the picture is still partial | [optional] 
**vol_proc** | **str** | Percentage of the expected operation volume already accepted for this base date | [optional] 
**qtd_ifs** | **float** | Number of financial institutions where the client has operations | [optional] 
**qtd_cong_finc** | **float** | Number of financial conglomerates where the client has operations | [optional] 
**dtb_ini_rel** | **str** | Start of the client&#39;s relationship with the national financial system | [optional] 
**coob_ass** | **float** | Co-obligation assumed by the client in credit assignments, in BRL | [optional] 
**coob_rec** | **float** | Co-obligation received in credit assignments, in BRL | [optional] 
**ls_op** | [**List[ScrOperation]**](ScrOperation.md) | Operation groups reported for this base date | [optional] 

## Example

```python
from pluggy_sdk.models.scr_database import ScrDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of ScrDatabase from a JSON string
scr_database_instance = ScrDatabase.from_json(json)
# print the JSON string representation of the object
print(ScrDatabase.to_json())

# convert the object into a dict
scr_database_dict = scr_database_instance.to_dict()
# create an instance of ScrDatabase from a dict
scr_database_from_dict = ScrDatabase.from_dict(scr_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


