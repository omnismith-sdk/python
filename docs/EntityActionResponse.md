# EntityActionResponse

A named, template-scoped operation on one record: a precondition that gates it, the fields the operator is asked for, and presets applied silently. Executing an action is one entity write that passes the template's rules like any other. A status transition is `precondition: [status eq draft]`, `presets: [status = confirmed]`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Action UUID | [optional] 
**template_id** | **UUID** | UUID of the template the action belongs to | [optional] 
**slug** | **str** | Identifier used in URLs and by agents; unique per template | [optional] 
**name** | **str** | Label shown in menus and dialogs | [optional] 
**description** | **str** | What the action does, shown in the dialog | [optional] 
**icon** | **str** | Material icon name | [optional] 
**is_enabled** | **bool** | Disabled actions are stored but neither listed for records nor executable | [optional] 
**precondition** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Conditions on the record&#39;s current values that must all hold for the action to be available. Empty means always available. | [optional] 
**fields** | [**List[EntityActionField]**](EntityActionField.md) | Values the operator is asked for, in dialog order | [optional] 
**presets** | [**List[EntityActionPreset]**](EntityActionPreset.md) | Values written silently on execution | [optional] 
**sort_order** | **int** | Position among the template&#39;s actions, zero-based | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.entity_action_response import EntityActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionResponse from a JSON string
entity_action_response_instance = EntityActionResponse.from_json(json)
# print the JSON string representation of the object
print(EntityActionResponse.to_json())

# convert the object into a dict
entity_action_response_dict = entity_action_response_instance.to_dict()
# create an instance of EntityActionResponse from a dict
entity_action_response_from_dict = EntityActionResponse.from_dict(entity_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


