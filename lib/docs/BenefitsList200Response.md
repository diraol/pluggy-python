# BenefitsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**results** | [**List[BenefitResponse]**](BenefitResponse.md) | List of benefits | [optional] 

## Example

```python
from pluggy_sdk.models.benefits_list200_response import BenefitsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitsList200Response from a JSON string
benefits_list200_response_instance = BenefitsList200Response.from_json(json)
# print the JSON string representation of the object
print(BenefitsList200Response.to_json())

# convert the object into a dict
benefits_list200_response_dict = benefits_list200_response_instance.to_dict()
# create an instance of BenefitsList200Response from a dict
benefits_list200_response_from_dict = BenefitsList200Response.from_dict(benefits_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


