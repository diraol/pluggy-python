# PixData

Payment Intent PIX data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | PIX QR raw value | 
**qr** | **str** | PIX QR image in base64 format | 

## Example

```python
from pluggy_sdk.models.pix_data import PixData

# TODO update the JSON string below
json = "{}"
# create an instance of PixData from a JSON string
pix_data_instance = PixData.from_json(json)
# print the JSON string representation of the object
print(PixData.to_json())

# convert the object into a dict
pix_data_dict = pix_data_instance.to_dict()
# create an instance of PixData from a dict
pix_data_form_dict = pix_data.from_dict(pix_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


