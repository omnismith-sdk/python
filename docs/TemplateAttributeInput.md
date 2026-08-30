# TemplateAttributeInput

Specification for associating an attribute with a template, including optional per-template default value. Specify either attribute_id or attribute_slug.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID. Specify either attribute_id or attribute_slug. | [optional] 
**attribute_slug** | **str** | Attribute unique slug. Specify either attribute_id or attribute_slug. | [optional] 
**default_value** | **str** | Default value applied to new entities when omitted. For List attributes, must be a valid list item UUID. For Reference attributes, a target entity UUID. For Metric/Number, a numeric string. For Boolean, \&quot;true\&quot; or \&quot;false\&quot;. For Date/Datetime, an ISO timestamp string. For File/Image, defaults are unsupported. Null means no default. | [optional] 

## Example

```python
from omnismith_sdk.models.template_attribute_input import TemplateAttributeInput

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateAttributeInput from a JSON string
template_attribute_input_instance = TemplateAttributeInput.from_json(json)
# print the JSON string representation of the object
print(TemplateAttributeInput.to_json())

# convert the object into a dict
template_attribute_input_dict = template_attribute_input_instance.to_dict()
# create an instance of TemplateAttributeInput from a dict
template_attribute_input_from_dict = TemplateAttributeInput.from_dict(template_attribute_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


