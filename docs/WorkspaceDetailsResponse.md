# WorkspaceDetailsResponse

Workspace details including configuration and fully hydrated view panes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Workspace unique identifier | [optional] 
**name** | **str** | Display name of the workspace | [optional] 
**description** | **str** | Detailed workspace description | [optional] 
**layout** | **str** | Multi-pane layout structure | [optional] 
**is_default** | **bool** | Whether this workspace is designated as the default project view | [optional] 
**sort_order** | **int** | Display ordering index in the workspace navigation switcher | [optional] 
**views** | [**List[WorkspaceViewResponse]**](WorkspaceViewResponse.md) | Ordered list of view panes attached to this workspace | [optional] 
**created_at** | **datetime** | ISO 8601 creation timestamp | [optional] 
**updated_at** | **datetime** | ISO 8601 last update timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.workspace_details_response import WorkspaceDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDetailsResponse from a JSON string
workspace_details_response_instance = WorkspaceDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceDetailsResponse.to_json())

# convert the object into a dict
workspace_details_response_dict = workspace_details_response_instance.to_dict()
# create an instance of WorkspaceDetailsResponse from a dict
workspace_details_response_from_dict = WorkspaceDetailsResponse.from_dict(workspace_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


