# InvestmentCouponPayment

Coupon-payment schedule for coupon-bearing fixed income / Treasury bonds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_coupon** | **bool** | Whether the paper pays periodic coupons | [optional] 
**periodicity** | **str** | Frequency of coupon payments (MONTHLY, QUARTERLY, SEMESTERLY, YEARLY, IRREGULAR) | [optional] 
**additional_info** | **str** | Free-text detail when periodicity is IRREGULAR | [optional] 

## Example

```python
from pluggy_sdk.models.investment_coupon_payment import InvestmentCouponPayment

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentCouponPayment from a JSON string
investment_coupon_payment_instance = InvestmentCouponPayment.from_json(json)
# print the JSON string representation of the object
print(InvestmentCouponPayment.to_json())

# convert the object into a dict
investment_coupon_payment_dict = investment_coupon_payment_instance.to_dict()
# create an instance of InvestmentCouponPayment from a dict
investment_coupon_payment_from_dict = InvestmentCouponPayment.from_dict(investment_coupon_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


