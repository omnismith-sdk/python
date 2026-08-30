# WorkspaceViewResponse

Workspace view / pane configuration including template binding, filters, search settings, and presentation modes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Workspace view unique identifier | [optional] 
**workspace_id** | **UUID** | Parent workspace unique identifier | [optional] 
**template_id** | **UUID** | Bound entity template unique identifier | [optional] 
**name** | **str** | Display name for the view pane tab or header | [optional] 
**filters** | **List[object]** | Dynamic filter rules applied to entities in this view | [optional] 
**search_string** | **str** | Active search query string | [optional] 
**search_mode** | **str** | Search execution mode | [optional] 
**sort** | [**WorkspaceViewResponseSort**](WorkspaceViewResponseSort.md) |  | [optional] 
**display_mode** | **str** | Presentation layout mode | [optional] 
**displayed_columns** | **List[str]** | List of displayed attribute slugs or UUIDs for table view | [optional] 
**pane_order** | **int** | Display sequence index of this pane within the workspace layout | [optional] 
**created_at** | **datetime** | ISO 8601 creation timestamp | [optional] 
**updated_at** | **datetime** | ISO 8601 last update timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.workspace_view_response import WorkspaceViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceViewResponse from a JSON string
workspace_view_response_instance = WorkspaceViewResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceViewResponse.to_json())

# convert the object into a dict
workspace_view_response_dict = workspace_view_response_instance.to_dict()
# create an instance of WorkspaceViewResponse from a dict
workspace_view_response_from_dict = WorkspaceViewResponse.from_dict(workspace_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


