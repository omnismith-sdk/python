# EntityActionPresetOverviewResponse

Preconfigured value written silently when this action executes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID to set | 
**attribute_slug** | **str** | Attribute slug identifier | [optional] 
**value** | **str** | Value to write silently | 

## Example

```python
from omnismith_sdk.models.entity_action_preset_overview_response import EntityActionPresetOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionPresetOverviewResponse from a JSON string
entity_action_preset_overview_response_instance = EntityActionPresetOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(EntityActionPresetOverviewResponse.to_json())

# convert the object into a dict
entity_action_preset_overview_response_dict = entity_action_preset_overview_response_instance.to_dict()
# create an instance of EntityActionPresetOverviewResponse from a dict
entity_action_preset_overview_response_from_dict = EntityActionPresetOverviewResponse.from_dict(entity_action_preset_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


