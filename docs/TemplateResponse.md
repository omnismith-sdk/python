# TemplateResponse

Template schema details including attribute bindings, default values, and visual groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Template UUID | [optional] 
**slug** | **str** | Unique template slug identifier | [optional] 
**name** | **str** | Human-readable template name | [optional] 
**description** | **str** | Template description | [optional] 
**category** | **str** | Template category for UI grouping | [optional] 
**attribute_ids** | **List[UUID]** | Flat list of associated attribute UUIDs | [optional] 
**attributes** | [**List[TemplateResponseAttributesInner]**](TemplateResponseAttributesInner.md) | Template attributes with their per-template default values. | [optional] 
**groups** | [**List[TemplateGroupResponse]**](TemplateGroupResponse.md) | Ordered attribute groups for organizing template fields into visual UI sections. | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**deleted_at** | **datetime** | Deletion timestamp if soft-deleted | [optional] 

## Example

```python
from omnismith_sdk.models.template_response import TemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateResponse from a JSON string
template_response_instance = TemplateResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateResponse.to_json())

# convert the object into a dict
template_response_dict = template_response_instance.to_dict()
# create an instance of TemplateResponse from a dict
template_response_from_dict = TemplateResponse.from_dict(template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


