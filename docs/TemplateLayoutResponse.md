# TemplateLayoutResponse

Visual layout configuration for organizing template fields into UI sections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | Template UUID | 
**category** | **str** | Template category for UI sidebar grouping | [optional] 
**groups** | [**List[TemplateGroupResponse]**](TemplateGroupResponse.md) | Ordered attribute groups for organizing fields into form sections | 

## Example

```python
from omnismith_sdk.models.template_layout_response import TemplateLayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateLayoutResponse from a JSON string
template_layout_response_instance = TemplateLayoutResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateLayoutResponse.to_json())

# convert the object into a dict
template_layout_response_dict = template_layout_response_instance.to_dict()
# create an instance of TemplateLayoutResponse from a dict
template_layout_response_from_dict = TemplateLayoutResponse.from_dict(template_layout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


