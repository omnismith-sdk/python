# TemplateResponseAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID | 
**default_value** | **str** | Per-template default value for newly created entities (or null) | [optional] 

## Example

```python
from omnismith_sdk.models.template_response_attributes_inner import TemplateResponseAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateResponseAttributesInner from a JSON string
template_response_attributes_inner_instance = TemplateResponseAttributesInner.from_json(json)
# print the JSON string representation of the object
print(TemplateResponseAttributesInner.to_json())

# convert the object into a dict
template_response_attributes_inner_dict = template_response_attributes_inner_instance.to_dict()
# create an instance of TemplateResponseAttributesInner from a dict
template_response_attributes_inner_from_dict = TemplateResponseAttributesInner.from_dict(template_response_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


