# CreateWorkspaceViewRequest

Payload for adding a new view / pane to a workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | Target template ID defining entity schema bound to this view pane | 
**name** | **str** | Display label for the view pane tab or header | 
**filters** | **List[object]** | Dynamic filtering rules applied to entities rendered in this view pane | [optional] 
**search_string** | **str** | Initial search query string applied to entities in this view | [optional] 
**search_mode** | **str** | Search execution mode (keyword text search or semantic vector similarity search) | [optional] [default to 'keyword']
**sort** | [**CreateWorkspaceViewRequestSort**](CreateWorkspaceViewRequestSort.md) |  | [optional] 
**display_mode** | **str** | Presentation layout type for entity records (table or card grid) | [optional] [default to 'table']
**displayed_columns** | **List[str]** | List of attribute slugs or UUIDs to display as columns in table mode | [optional] 
**pane_order** | **int** | Display sequence index of this pane within the workspace layout | [optional] 

## Example

```python
from omnismith_sdk.models.create_workspace_view_request import CreateWorkspaceViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceViewRequest from a JSON string
create_workspace_view_request_instance = CreateWorkspaceViewRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceViewRequest.to_json())

# convert the object into a dict
create_workspace_view_request_dict = create_workspace_view_request_instance.to_dict()
# create an instance of CreateWorkspaceViewRequest from a dict
create_workspace_view_request_from_dict = CreateWorkspaceViewRequest.from_dict(create_workspace_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


