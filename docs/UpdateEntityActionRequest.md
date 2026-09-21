# UpdateEntityActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Identifier used in URLs and by agents; unique per template. Lowercase letters, digits and underscores, starting with a letter. | 
**name** | **str** | Label shown in menus and dialogs | 
**description** | **str** | What the action does, shown in the dialog | [optional] 
**icon** | **str** | Material icon name | [optional] 
**precondition** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Full replacement of the precondition; empty for an action that is always available | [optional] 
**fields** | [**List[EntityActionField]**](EntityActionField.md) | Full replacement of the fields, in dialog order | [optional] 
**presets** | [**List[EntityActionPreset]**](EntityActionPreset.md) | Full replacement of the presets | [optional] 

## Example

```python
from omnismith_sdk.models.update_entity_action_request import UpdateEntityActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityActionRequest from a JSON string
update_entity_action_request_instance = UpdateEntityActionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityActionRequest.to_json())

# convert the object into a dict
update_entity_action_request_dict = update_entity_action_request_instance.to_dict()
# create an instance of UpdateEntityActionRequest from a dict
update_entity_action_request_from_dict = UpdateEntityActionRequest.from_dict(update_entity_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


