# PatchAttributeRequest

Payload for partial attribute modification. All fields are optional; only provided properties will be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New human-readable name for the attribute. | [optional] 
**template_ids** | **List[UUID]** | Updated array of template UUIDs to associate. When provided, replaces the template list while safely merging restricted templates. | [optional] 
**description** | **str** | New descriptive text for the attribute. Pass null to clear. | [optional] 
**reference_config** | [**PatchAttributeRequestReferenceConfig**](PatchAttributeRequestReferenceConfig.md) |  | [optional] 
**data_type** | **int** | Target data type for lossless transition on Dimension (0) attributes: Number(1)-&gt;String(0), Boolean(2)-&gt;String(0), Date(4)&lt;-&gt;Datetime(3), Date/Datetime-&gt;String(0), String(0)&lt;-&gt;Markdown(7). | [optional] 
**slug** | **str** | New unique slug identifier within the project. | [optional] 

## Example

```python
from omnismith_sdk.models.patch_attribute_request import PatchAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAttributeRequest from a JSON string
patch_attribute_request_instance = PatchAttributeRequest.from_json(json)
# print the JSON string representation of the object
print(PatchAttributeRequest.to_json())

# convert the object into a dict
patch_attribute_request_dict = patch_attribute_request_instance.to_dict()
# create an instance of PatchAttributeRequest from a dict
patch_attribute_request_from_dict = PatchAttributeRequest.from_dict(patch_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


