# EntityAttributeValue

Structured attribute value representation including raw serialized value, resolved display value for references and list items, and attribute metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Raw serialized attribute value (string, numeric string, ISO date, or UUID) | [optional] 
**custom_value** | **str** | Resolved display label or custom representation (for list options, reference entities, or formatted values) | [optional] 
**reference_entity_id** | **UUID** | Target entity UUID when the attribute kind is reference | [optional] 
**attribute_id** | **UUID** | Canonical attribute definition UUID | [optional] 
**attribute_slug** | **str** | Human-readable attribute slug identifier | [optional] 

## Example

```python
from omnismith_sdk.models.entity_attribute_value import EntityAttributeValue

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAttributeValue from a JSON string
entity_attribute_value_instance = EntityAttributeValue.from_json(json)
# print the JSON string representation of the object
print(EntityAttributeValue.to_json())

# convert the object into a dict
entity_attribute_value_dict = entity_attribute_value_instance.to_dict()
# create an instance of EntityAttributeValue from a dict
entity_attribute_value_from_dict = EntityAttributeValue.from_dict(entity_attribute_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


