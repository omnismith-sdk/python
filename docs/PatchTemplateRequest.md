# PatchTemplateRequest

Payload for partial template modification. All properties are optional; only supplied values are updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[TemplateAttributeInput]**](TemplateAttributeInput.md) | Structured template attributes with optional per-template default values. If provided, replaces attribute associations. | [optional] 
**groups** | [**List[TemplateGroupInput]**](TemplateGroupInput.md) | Ordered attribute groups for organizing template fields into visual UI sections. | [optional] 
**name** | **str** | New human-readable name of the template. | [optional] 
**description** | **str** | New description for the template. | [optional] 
**category** | **str** | New category tag for navigation grouping. | [optional] 
**attribute_ids** | **List[UUID]** | Flat list of attribute UUIDs to associate. | [optional] 
**attribute_slugs** | **List[str]** | Flat list of attribute slugs to associate. | [optional] 
**slug** | **str** | New unique slug identifier within the project. | [optional] 

## Example

```python
from omnismith_sdk.models.patch_template_request import PatchTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchTemplateRequest from a JSON string
patch_template_request_instance = PatchTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchTemplateRequest.to_json())

# convert the object into a dict
patch_template_request_dict = patch_template_request_instance.to_dict()
# create an instance of PatchTemplateRequest from a dict
patch_template_request_from_dict = PatchTemplateRequest.from_dict(patch_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


