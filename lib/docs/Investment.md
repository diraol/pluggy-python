# Investment

Investment representing a specific asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**item_id** | **str** | Identifier of the item linked to the investment | 
**type** | **str** | Investment Asset type | 
**subtype** | **str** | Investment subtype, depends on the type | [optional] 
**number** | **str** | Reference number for this holder&#39;s asset | [optional] 
**balance** | **float** | The current net balance amount of the investment | 
**name** | **str** | Name on the provider | 
**last_month_rate** | **float** | The performance rate of the investment in the last month | [optional] 
**last_twelve_months_rate** | **float** | The performance rate of the investment in the last 12 months | [optional] 
**annual_rate** | **float** | The performance rate of the investment in the last year | [optional] 
**currency_code** | **str** | Currency ISO code for the amounts | 
**code** | **str** | Associated Code for the investment. For example, the code for a mutual fund is the CNPJ | [optional] 
**isin** | **str** | 12-character ISIN, a globally unique identifier | [optional] 
**value** | **float** | Quota&#39;s current value at \&quot;date\&quot; | [optional] 
**quantity** | **float** | Quantity of quota at disposal | [optional] 
**amount** | **float** | Gross amount of the investment | [optional] 
**taxes** | **float** | Income taxes applied to the investment | [optional] 
**taxes2** | **float** | Financial taxes applied to the investment | [optional] 
**var_date** | **datetime** | Value&#39;s quota date | 
**owner** | **str** | Owner/beneficiary associated with the investment | [optional] 
**amount_profit** | **float** | Profit/Loss to date over the investment | [optional] 
**amount_withdrawal** | **float** | The amount available to withdraw | [optional] 
**amount_original** | **float** | Amount originally invested | [optional] 
**metadata** | [**InvestmentMetadata**](InvestmentMetadata.md) |  | [optional] 
**transactions** | [**List[InvestmentTransaction]**](InvestmentTransaction.md) | (DEPRECATED: this field will be removed for new applications created from 21st March 2023 onward. Use the paginated &#x60;GET /investment/{id}/transactions&#x60; endpoint instead.) Transactions made on the investment (Buy, Sell, Transfer, Tax) | [optional] 
**due_date** | **datetime** | Expiration Date | [optional] 
**issuer** | **str** | The entity that issued the investment | [optional] 
**issuer_cnpj** | **str** | The entity CNPJ that issued the investment | [optional] 
**issue_date** | **datetime** | The date that the investment was issued | [optional] 
**rate** | **float** | Fixed rate percentage applied to the investment | [optional] 
**rate_type** | **str** | Type of fixed-rate | [optional] 
**fixed_annual_rate** | **float** | Fixed income annual rate | [optional] 
**status** | **str** | Current status of the investment enum value | [optional] 

## Example

```python
from openapi_client.models.investment import Investment

# TODO update the JSON string below
json = "{}"
# create an instance of Investment from a JSON string
investment_instance = Investment.from_json(json)
# print the JSON string representation of the object
print(Investment.to_json())

# convert the object into a dict
investment_dict = investment_instance.to_dict()
# create an instance of Investment from a dict
investment_form_dict = investment.from_dict(investment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


