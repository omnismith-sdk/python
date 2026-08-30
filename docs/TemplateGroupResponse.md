# TemplateGroupResponse

Visual attribute group details for organizing template fields into UI sections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique group UUID | 
**name** | **str** | Group display title / section heading | 
**description** | **str** | Optional group descriptive subtitle | [optional] 
**icon** | **str** | Optional icon name for the section header | [optional] 
**columns** | **int** | Grid column layout count (1 or 2) | 
**attribute_ids** | **List[UUID]** | Ordered list of attribute UUIDs assigned to this section group. | 

## Example

```python
from omnismith_sdk.models.template_group_response import TemplateGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateGroupResponse from a JSON string
template_group_response_instance = TemplateGroupResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateGroupResponse.to_json())

# convert the object into a dict
template_group_response_dict = template_group_response_instance.to_dict()
# create an instance of TemplateGroupResponse from a dict
template_group_response_from_dict = TemplateGroupResponse.from_dict(template_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


