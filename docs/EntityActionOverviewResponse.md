# EntityActionOverviewResponse

Template-scoped business action (e.g. status transition, workflow action).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Action UUID | 
**slug** | **str** | Action slug identifier | 
**name** | **str** | Human-readable action name | 
**description** | **str** | Action description | [optional] 
**is_enabled** | **bool** | Whether the action is active and executable | 
**precondition** | [**List[EntityRulePredicateOverviewResponse]**](EntityRulePredicateOverviewResponse.md) | Conditions that must hold on the record for the action to be available | 
**fields** | [**List[EntityActionFieldOverviewResponse]**](EntityActionFieldOverviewResponse.md) | Fields prompted from the operator | 
**presets** | [**List[EntityActionPresetOverviewResponse]**](EntityActionPresetOverviewResponse.md) | Values written silently upon execution | 

## Example

```python
from omnismith_sdk.models.entity_action_overview_response import EntityActionOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionOverviewResponse from a JSON string
entity_action_overview_response_instance = EntityActionOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(EntityActionOverviewResponse.to_json())

# convert the object into a dict
entity_action_overview_response_dict = entity_action_overview_response_instance.to_dict()
# create an instance of EntityActionOverviewResponse from a dict
entity_action_overview_response_from_dict = EntityActionOverviewResponse.from_dict(entity_action_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


