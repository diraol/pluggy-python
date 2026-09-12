# ScrMaturityBalances

Balance of the operation group split across Bacen's maturity vertices, in BRL. Each key is a vertex code and belongs to one of three families: amounts not yet due (a payment up to 14 days late still counts here), amounts overdue graded by how old the delay is, and a few categories that are not time windows at all. The window behind each individual code is defined by Bacen's DOC3040 reference — read it there rather than inferring it from the number. Only the vertices that carry a value are present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v20** | **float** |  | [optional] 
**v40** | **float** |  | [optional] 
**v60** | **float** |  | [optional] 
**v80** | **float** |  | [optional] 
**v110** | **float** |  | [optional] 
**v120** | **float** |  | [optional] 
**v130** | **float** |  | [optional] 
**v140** | **float** |  | [optional] 
**v150** | **float** |  | [optional] 
**v160** | **float** |  | [optional] 
**v165** | **float** |  | [optional] 
**v170** | **float** |  | [optional] 
**v175** | **float** |  | [optional] 
**v180** | **float** |  | [optional] 
**v190** | **float** |  | [optional] 
**v199** | **float** |  | [optional] 
**v205** | **float** |  | [optional] 
**v210** | **float** |  | [optional] 
**v220** | **float** |  | [optional] 
**v230** | **float** |  | [optional] 
**v240** | **float** |  | [optional] 
**v245** | **float** |  | [optional] 
**v250** | **float** |  | [optional] 
**v255** | **float** |  | [optional] 
**v260** | **float** |  | [optional] 
**v270** | **float** |  | [optional] 
**v280** | **float** |  | [optional] 
**v290** | **float** |  | [optional] 
**v310** | **float** |  | [optional] 
**v320** | **float** |  | [optional] 

## Example

```python
from pluggy_sdk.models.scr_maturity_balances import ScrMaturityBalances

# TODO update the JSON string below
json = "{}"
# create an instance of ScrMaturityBalances from a JSON string
scr_maturity_balances_instance = ScrMaturityBalances.from_json(json)
# print the JSON string representation of the object
print(ScrMaturityBalances.to_json())

# convert the object into a dict
scr_maturity_balances_dict = scr_maturity_balances_instance.to_dict()
# create an instance of ScrMaturityBalances from a dict
scr_maturity_balances_from_dict = ScrMaturityBalances.from_dict(scr_maturity_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


