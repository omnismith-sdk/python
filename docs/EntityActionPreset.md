# EntityActionPreset

One value the action writes silently when it runs. Presets win over submitted values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID to set. Must belong to the template and must not be a metric or a field of the same action. | 
**value** | **str** | Value serialized as a string: a list item UUID for list attributes, an entity UUID for references, &#x60;true&#x60;/&#x60;false&#x60; for booleans, a number or date as text. | 

## Example

```python
from omnismith_sdk.models.entity_action_preset import EntityActionPreset

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionPreset from a JSON string
entity_action_preset_instance = EntityActionPreset.from_json(json)
# print the JSON string representation of the object
print(EntityActionPreset.to_json())

# convert the object into a dict
entity_action_preset_dict = entity_action_preset_instance.to_dict()
# create an instance of EntityActionPreset from a dict
entity_action_preset_from_dict = EntityActionPreset.from_dict(entity_action_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


