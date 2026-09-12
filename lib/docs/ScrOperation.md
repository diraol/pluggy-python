# ScrOperation

A group of credit operations. The SCR does not return contracts one by one: it aggregates them by the combination of modality, source of funds, index and exchange variation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | **str** | Bacen&#39;s code for the operation modality | [optional] 
**ori_rec** | **str** | Bacen&#39;s code for the source of funds | [optional] 
**indx** | **str** | Bacen&#39;s code for the reference rate or index | [optional] 
**var_camb** | **str** | Bacen&#39;s code for the exchange rate variation | [optional] 
**sub_j_disc** | **str** | Present when the operation is under dispute: \&quot;D\&quot; for disagreement, \&quot;J\&quot; for sub judice, \&quot;JD\&quot; for both | [optional] 
**res_venc** | [**ScrMaturityBalances**](ScrMaturityBalances.md) |  | [optional] 
**ls_gar** | [**List[ScrGuarantee]**](ScrGuarantee.md) | Guarantees backing the operations in this group | [optional] 
**ls_inf_ad** | [**List[ScrAdditionalInfo]**](ScrAdditionalInfo.md) | Complementary information reported for this group | [optional] 

## Example

```python
from pluggy_sdk.models.scr_operation import ScrOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ScrOperation from a JSON string
scr_operation_instance = ScrOperation.from_json(json)
# print the JSON string representation of the object
print(ScrOperation.to_json())

# convert the object into a dict
scr_operation_dict = scr_operation_instance.to_dict()
# create an instance of ScrOperation from a dict
scr_operation_from_dict = ScrOperation.from_dict(scr_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


