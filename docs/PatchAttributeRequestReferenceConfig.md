# PatchAttributeRequestReferenceConfig

Updated reference configuration for Reference (3) attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_template_id** | **UUID** | Target template UUID | [optional] 
**target_attribute_id** | **UUID** | Target display attribute UUID | [optional] 

## Example

```python
from omnismith_sdk.models.patch_attribute_request_reference_config import PatchAttributeRequestReferenceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAttributeRequestReferenceConfig from a JSON string
patch_attribute_request_reference_config_instance = PatchAttributeRequestReferenceConfig.from_json(json)
# print the JSON string representation of the object
print(PatchAttributeRequestReferenceConfig.to_json())

# convert the object into a dict
patch_attribute_request_reference_config_dict = patch_attribute_request_reference_config_instance.to_dict()
# create an instance of PatchAttributeRequestReferenceConfig from a dict
patch_attribute_request_reference_config_from_dict = PatchAttributeRequestReferenceConfig.from_dict(patch_attribute_request_reference_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


