# WorkspaceResponse

Workspace summary details including layout and pane counts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Workspace unique identifier | [optional] 
**name** | **str** | Display name of the workspace | [optional] 
**description** | **str** | Detailed workspace description | [optional] 
**layout** | **str** | Multi-pane layout structure | [optional] 
**is_default** | **bool** | Whether this workspace serves as the default project landing view | [optional] 
**sort_order** | **int** | Display ordering index in the workspace navigation switcher | [optional] 
**view_count** | **int** | Number of view panes currently attached to this workspace | [optional] 
**created_at** | **datetime** | ISO 8601 creation timestamp | [optional] 
**updated_at** | **datetime** | ISO 8601 last update timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.workspace_response import WorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceResponse from a JSON string
workspace_response_instance = WorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceResponse.to_json())

# convert the object into a dict
workspace_response_dict = workspace_response_instance.to_dict()
# create an instance of WorkspaceResponse from a dict
workspace_response_from_dict = WorkspaceResponse.from_dict(workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


