# EntityActionAvailablePreset

A value the action writes silently; shown so the operator knows what will change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** |  | 
**slug** | **str** |  | 
**name** | **str** |  | 
**value** | **str** | The stored value: a list item id, an entity id, &#x60;true&#x60;/&#x60;false&#x60;, a number or date as text | 
**display_value** | **str** | The list item label for list attributes, otherwise the value itself | 

## Example

```python
from omnismith_sdk.models.entity_action_available_preset import EntityActionAvailablePreset

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionAvailablePreset from a JSON string
entity_action_available_preset_instance = EntityActionAvailablePreset.from_json(json)
# print the JSON string representation of the object
print(EntityActionAvailablePreset.to_json())

# convert the object into a dict
entity_action_available_preset_dict = entity_action_available_preset_instance.to_dict()
# create an instance of EntityActionAvailablePreset from a dict
entity_action_available_preset_from_dict = EntityActionAvailablePreset.from_dict(entity_action_available_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


