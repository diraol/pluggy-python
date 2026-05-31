# AccountBalanceGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | The available balance of the account, same as balance in the account resource. | 
**currency_code** | **str** | The currency code of the balance amounts | 
**update_date_time** | **str** | The date and time when the balance was last updated | 

## Example

```python
from pluggy_sdk.models.account_balance_get200_response import AccountBalanceGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBalanceGet200Response from a JSON string
account_balance_get200_response_instance = AccountBalanceGet200Response.from_json(json)
# print the JSON string representation of the object
print(AccountBalanceGet200Response.to_json())

# convert the object into a dict
account_balance_get200_response_dict = account_balance_get200_response_instance.to_dict()
# create an instance of AccountBalanceGet200Response from a dict
account_balance_get200_response_from_dict = AccountBalanceGet200Response.from_dict(account_balance_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


