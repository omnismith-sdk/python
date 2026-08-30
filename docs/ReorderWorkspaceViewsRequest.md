# ReorderWorkspaceViewsRequest

Payload containing the reordered list of workspace view IDs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_ids** | **List[UUID]** | Ordered array of view unique identifiers (UUIDs) defining the new pane sequence | 

## Example

```python
from omnismith_sdk.models.reorder_workspace_views_request import ReorderWorkspaceViewsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderWorkspaceViewsRequest from a JSON string
reorder_workspace_views_request_instance = ReorderWorkspaceViewsRequest.from_json(json)
# print the JSON string representation of the object
print(ReorderWorkspaceViewsRequest.to_json())

# convert the object into a dict
reorder_workspace_views_request_dict = reorder_workspace_views_request_instance.to_dict()
# create an instance of ReorderWorkspaceViewsRequest from a dict
reorder_workspace_views_request_from_dict = ReorderWorkspaceViewsRequest.from_dict(reorder_workspace_views_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


