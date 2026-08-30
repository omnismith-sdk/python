# WorkspaceViewResponseSort

Active sort configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **str** | Target field or column sorted by | [optional] 
**direction** | **str** | Sort direction | [optional] 

## Example

```python
from omnismith_sdk.models.workspace_view_response_sort import WorkspaceViewResponseSort

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceViewResponseSort from a JSON string
workspace_view_response_sort_instance = WorkspaceViewResponseSort.from_json(json)
# print the JSON string representation of the object
print(WorkspaceViewResponseSort.to_json())

# convert the object into a dict
workspace_view_response_sort_dict = workspace_view_response_sort_instance.to_dict()
# create an instance of WorkspaceViewResponseSort from a dict
workspace_view_response_sort_from_dict = WorkspaceViewResponseSort.from_dict(workspace_view_response_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


