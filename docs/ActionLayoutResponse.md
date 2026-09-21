# ActionLayoutResponse

Visual UI presentation details for an entity action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **UUID** | Action UUID | 
**template_id** | **UUID** | Template UUID | 
**icon** | **str** | Material icon identifier for action buttons and dialogs | [optional] 
**sort_order** | **int** | Display sorting rank in action menus | 

## Example

```python
from omnismith_sdk.models.action_layout_response import ActionLayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionLayoutResponse from a JSON string
action_layout_response_instance = ActionLayoutResponse.from_json(json)
# print the JSON string representation of the object
print(ActionLayoutResponse.to_json())

# convert the object into a dict
action_layout_response_dict = action_layout_response_instance.to_dict()
# create an instance of ActionLayoutResponse from a dict
action_layout_response_from_dict = ActionLayoutResponse.from_dict(action_layout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


