# ReservedBalanceRemuneration

Remuneration applied to a reserved balance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_fixed_rate** | **float** | Pre-fixed remuneration rate, as a fraction (for example, 0.3 &#x3D; 30%) | [optional] 
**post_fixed_indexer_percentage** | **float** | Post-fixed indexer percentage, as a fraction (for example, 1.1 &#x3D; 110% of the indexer) | [optional] 
**rate_type** | **str** | Rate type (LINEAR or EXPONENCIAL) | [optional] 
**indexer** | **str** | Indexer used as remuneration reference (for example, CDI, IPCA, SELIC) | [optional] 
**calculation** | **str** | Calculation basis (DIAS_UTEIS or DIAS_CORRIDOS) | [optional] 
**rate_periodicity** | **str** | Rate periodicity (MENSAL, ANUAL, DIARIO or SEMESTRAL) | [optional] 
**indexer_additional_info** | **str** | Additional indexer info, required when indexer is OUTROS | [optional] 

## Example

```python
from pluggy_sdk.models.reserved_balance_remuneration import ReservedBalanceRemuneration

# TODO update the JSON string below
json = "{}"
# create an instance of ReservedBalanceRemuneration from a JSON string
reserved_balance_remuneration_instance = ReservedBalanceRemuneration.from_json(json)
# print the JSON string representation of the object
print(ReservedBalanceRemuneration.to_json())

# convert the object into a dict
reserved_balance_remuneration_dict = reserved_balance_remuneration_instance.to_dict()
# create an instance of ReservedBalanceRemuneration from a dict
reserved_balance_remuneration_from_dict = ReservedBalanceRemuneration.from_dict(reserved_balance_remuneration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


