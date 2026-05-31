# IdentityResponseQualificationsInformedPatrimony

Informed patrimony

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the informed patrimony | 
**year** | **float** | Year of the patrimony | 
**var_date** | **datetime** | Reference date of the patrimony. Returned on the business path of Open Finance, where the source field is a full date rather than just a year | [optional] 

## Example

```python
from pluggy_sdk.models.identity_response_qualifications_informed_patrimony import IdentityResponseQualificationsInformedPatrimony

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityResponseQualificationsInformedPatrimony from a JSON string
identity_response_qualifications_informed_patrimony_instance = IdentityResponseQualificationsInformedPatrimony.from_json(json)
# print the JSON string representation of the object
print(IdentityResponseQualificationsInformedPatrimony.to_json())

# convert the object into a dict
identity_response_qualifications_informed_patrimony_dict = identity_response_qualifications_informed_patrimony_instance.to_dict()
# create an instance of IdentityResponseQualificationsInformedPatrimony from a dict
identity_response_qualifications_informed_patrimony_from_dict = IdentityResponseQualificationsInformedPatrimony.from_dict(identity_response_qualifications_informed_patrimony_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


