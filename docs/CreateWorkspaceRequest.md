# CreateWorkspaceRequest

Payload for creating a new workspace workbench

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable display name of the workspace | 
**description** | **str** | Detailed description of the workspace purpose and workflow | [optional] 
**layout** | **str** | Multi-pane grid layout arrangement | [optional] [default to 'split-v']
**is_default** | **bool** | Whether this workspace serves as the default landing view for the project | [optional] [default to False]
**initial_template_ids** | **List[UUID]** | Optional list of entity template IDs to automatically create and mount as initial view panes | [optional] 

## Example

```python
from omnismith_sdk.models.create_workspace_request import CreateWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceRequest from a JSON string
create_workspace_request_instance = CreateWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceRequest.to_json())

# convert the object into a dict
create_workspace_request_dict = create_workspace_request_instance.to_dict()
# create an instance of CreateWorkspaceRequest from a dict
create_workspace_request_from_dict = CreateWorkspaceRequest.from_dict(create_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


