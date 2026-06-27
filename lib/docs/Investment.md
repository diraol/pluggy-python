# Investment

Investment representing a specific asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier | 
**item_id** | **UUID** | Identifier of the item linked to the investment | 
**type** | **str** | Investment asset class. - &#x60;MUTUAL_FUND&#x60;: actively managed pooled investment funds (FIM, FIA, FIC). - &#x60;EQUITY&#x60;: stocks and equity-like assets traded on a stock exchange. - &#x60;ETF&#x60;: Exchange Traded Funds. - &#x60;FIXED_INCOME&#x60;: fixed income products such as CDB, LCI, LCA, debentures, Tesouro Direto. - &#x60;COE&#x60;: Certificado de Operações Estruturadas (structured notes). - &#x60;SECURITY&#x60;: private pension / previdência products (PGBL, VGBL). - &#x60;OTHER&#x60;: any asset not covered by the categories above. | 
**subtype** | **str** | Specific instrument within a &#x60;type&#x60;. Possible groupings:  **EQUITY**: &#x60;STOCK&#x60; (ação), &#x60;BDR&#x60; (Brazilian Depositary Receipt), &#x60;REAL_ESTATE_FUND&#x60; (FII), &#x60;DERIVATIVES&#x60;, &#x60;OPTION&#x60;.  **ETF**: &#x60;ETF&#x60;.  **FIXED_INCOME**: &#x60;TREASURY&#x60; (Tesouro Direto), &#x60;CDB&#x60;, &#x60;LCI&#x60;, &#x60;LCA&#x60;, &#x60;LC&#x60;, &#x60;LF&#x60;, &#x60;CRI&#x60;, &#x60;CRA&#x60;, &#x60;DEBENTURES&#x60;, &#x60;CORPORATE_DEBT&#x60;.  **MUTUAL_FUND**: &#x60;INVESTMENT_FUND&#x60;, &#x60;MULTIMARKET_FUND&#x60;, &#x60;FIXED_INCOME_FUND&#x60;, &#x60;STOCK_FUND&#x60;, &#x60;ETF_FUND&#x60;, &#x60;OFFSHORE_FUND&#x60;, &#x60;FIP_FUND&#x60;, &#x60;EXCHANGE_FUND&#x60;, &#x60;FI_INFRA&#x60;, &#x60;FI_AGRO&#x60;.  **COE**: &#x60;STRUCTURED_NOTE&#x60;.  **SECURITY**: &#x60;RETIREMENT&#x60; (PGBL/VGBL).  **OTHER**: &#x60;OTHER&#x60;. | [optional] 
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
**metadata** | [**InvestmentMetadata**](InvestmentMetadata.md) | Security Portability details | [optional] 
**due_date** | **datetime** | Expiration Date | [optional] 
**issuer** | **str** | The entity that issued the investment | [optional] 
**issuer_cnpj** | **str** | The entity CNPJ that issued the investment | [optional] 
**issue_date** | **datetime** | The date that the investment was issued | [optional] 
**purchase_date** | **datetime** | The date that the investment was purchased | [optional] 
**grace_period_date** | **datetime** | The date when the grace period ends (fixed-income investments only) | [optional] 
**rate** | **float** | Fixed rate percentage applied to the investment | [optional] 
**rate_type** | **str** | Type of fixed-rate | [optional] 
**fixed_annual_rate** | **float** | Fixed income annual rate | [optional] 
**tax_exempt** | **bool** | Whether the product is tax-exempt (LCI, LCA, CRI, CRA, debêntures incentivadas) | [optional] 
**rate_periodicity** | **str** | Periodicity of the remuneration rate (DAILY, MONTHLY, SEMESTERLY, YEARLY) | [optional] 
**indexer_additional_info** | **str** | Free-text indexer description when the indexer is non-standard | [optional] 
**price_factor** | **float** | B3 lot/price conversion factor (variable income) | [optional] 
**debtor** | [**InvestmentDebtor**](InvestmentDebtor.md) |  | [optional] 
**coupon_payment** | [**InvestmentCouponPayment**](InvestmentCouponPayment.md) |  | [optional] 
**status** | **str** | Current lifecycle status of the investment. - &#x60;ACTIVE&#x60;: the investment is open and currently held by the owner. - &#x60;PENDING&#x60;: the operation has been requested but is not yet settled (e.g. a fund subscription within the settlement window). - &#x60;TOTAL_WITHDRAWAL&#x60;: the position has been fully redeemed/withdrawn; balance is zero. | [optional] 

## Example

```python
from pluggy_sdk.models.investment import Investment

# TODO update the JSON string below
json = "{}"
# create an instance of Investment from a JSON string
investment_instance = Investment.from_json(json)
# print the JSON string representation of the object
print(Investment.to_json())

# convert the object into a dict
investment_dict = investment_instance.to_dict()
# create an instance of Investment from a dict
investment_from_dict = Investment.from_dict(investment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


