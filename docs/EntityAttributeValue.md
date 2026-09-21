# EntityAttributeValue

Verbose attribute value item returned when `verbose=true`: raw serialized value, resolved display label for references and list items, and the attribute identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Canonical attribute definition UUID | 
**slug** | **str** | Human-readable attribute slug identifier; null when the attribute has no slug | 
**value** | **str** | Raw serialized attribute value (string, numeric string, ISO date, or UUID); empty string when unset | 
**custom_value** | **str** | Resolved display label (list option label, referenced entity display value, original filename) or the raw value for scalars | 
**reference_entity_id** | **UUID** | Target entity UUID when the attribute kind is reference | 

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


