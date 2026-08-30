# TemplateGroupInput

Visual attribute grouping specification for template forms and workbench views.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Optional group UUID. Auto-generated if omitted. | [optional] 
**name** | **str** | Group display title / section heading | 
**description** | **str** | Optional group descriptive subtitle | [optional] 
**icon** | **str** | Optional icon name for the section header | [optional] 
**columns** | **int** | Grid column layout count (1 or 2) | [optional] [default to 2]
**attribute_ids** | **List[UUID]** | Ordered list of attribute UUIDs assigned to this section group. | [optional] 

## Example

```python
from omnismith_sdk.models.template_group_input import TemplateGroupInput

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateGroupInput from a JSON string
template_group_input_instance = TemplateGroupInput.from_json(json)
# print the JSON string representation of the object
print(TemplateGroupInput.to_json())

# convert the object into a dict
template_group_input_dict = template_group_input_instance.to_dict()
# create an instance of TemplateGroupInput from a dict
template_group_input_from_dict = TemplateGroupInput.from_dict(template_group_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


