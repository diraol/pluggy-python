# IdentityResponseFinancialRelationshipsAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compe_code** | **str** | COMPE code of the account | 
**branch_code** | **str** | Branch code of the account | 
**number** | **str** | Number of the account | 
**check_digit** | **str** | Check digit of the account | 
**type** | **str** | Type of the account | 
**subtype** | **str** | Subtype of the account | 

## Example

```python
from pluggy_sdk.models.identity_response_financial_relationships_accounts_inner import IdentityResponseFinancialRelationshipsAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityResponseFinancialRelationshipsAccountsInner from a JSON string
identity_response_financial_relationships_accounts_inner_instance = IdentityResponseFinancialRelationshipsAccountsInner.from_json(json)
# print the JSON string representation of the object
print(IdentityResponseFinancialRelationshipsAccountsInner.to_json())

# convert the object into a dict
identity_response_financial_relationships_accounts_inner_dict = identity_response_financial_relationships_accounts_inner_instance.to_dict()
# create an instance of IdentityResponseFinancialRelationshipsAccountsInner from a dict
identity_response_financial_relationships_accounts_inner_from_dict = IdentityResponseFinancialRelationshipsAccountsInner.from_dict(identity_response_financial_relationships_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


