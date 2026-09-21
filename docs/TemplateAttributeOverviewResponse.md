# TemplateAttributeOverviewResponse

Template attribute association with optional per-template default value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Attribute UUID | 
**slug** | **str** | Attribute slug identifier | [optional] 
**default_value** | **str** | Per-template default value for newly created entities | [optional] 

## Example

```python
from omnismith_sdk.models.template_attribute_overview_response import TemplateAttributeOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateAttributeOverviewResponse from a JSON string
template_attribute_overview_response_instance = TemplateAttributeOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateAttributeOverviewResponse.to_json())

# convert the object into a dict
template_attribute_overview_response_dict = template_attribute_overview_response_instance.to_dict()
# create an instance of TemplateAttributeOverviewResponse from a dict
template_attribute_overview_response_from_dict = TemplateAttributeOverviewResponse.from_dict(template_attribute_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


