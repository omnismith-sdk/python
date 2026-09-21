# CreateWorkspaceRequest

Payload for creating a new top-level operational workspace workbench

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable display name of the workspace (e.g. \&quot;Editorial &amp; Content Calendar\&quot;, \&quot;Guidelines &amp; Strategy\&quot;, \&quot;Media Studio\&quot;) | 
**description** | **str** | Detailed description of the workspace purpose and operational domain | [optional] 
**layout** | **str** | Multi-pane grid layout arrangement (single, split-v, split-h, quad) | [optional] [default to 'single']
**is_default** | **bool** | Whether this workspace serves as the default landing view for the project | [optional] [default to False]
**initial_template_ids** | **List[str]** | Optional list of entity template UUIDs or slugs to automatically create and mount as initial view panes in this workspace | [optional] 

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


