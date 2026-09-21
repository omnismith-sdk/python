# CreateEntityActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Identifier used in URLs and by agents; unique per template. Lowercase letters, digits and underscores, starting with a letter. | 
**name** | **str** | Label shown in menus and dialogs | 
**description** | **str** | What the action does, shown in the dialog | [optional] 
**icon** | **str** | Material icon name | [optional] 
**precondition** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Conditions on the record&#39;s current values that must all hold for the action to be available. Omit or send an empty list for an action that is always available. | [optional] 
**fields** | [**List[EntityActionField]**](EntityActionField.md) | Values the operator is asked for, in dialog order. Each attribute may appear once and must not also be a preset. | [optional] 
**presets** | [**List[EntityActionPreset]**](EntityActionPreset.md) | Values written silently on execution. Each attribute may appear once and must not also be a field. | [optional] 

## Example

```python
from omnismith_sdk.models.create_entity_action_request import CreateEntityActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityActionRequest from a JSON string
create_entity_action_request_instance = CreateEntityActionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEntityActionRequest.to_json())

# convert the object into a dict
create_entity_action_request_dict = create_entity_action_request_instance.to_dict()
# create an instance of CreateEntityActionRequest from a dict
create_entity_action_request_from_dict = CreateEntityActionRequest.from_dict(create_entity_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


