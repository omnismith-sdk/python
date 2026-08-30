# CreateWorkspaceViewRequestSort

Active sort configuration defining target field and direction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **str** | Attribute key or system column to sort by | [optional] 
**direction** | **str** | Sort ordering direction | [optional] 

## Example

```python
from omnismith_sdk.models.create_workspace_view_request_sort import CreateWorkspaceViewRequestSort

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceViewRequestSort from a JSON string
create_workspace_view_request_sort_instance = CreateWorkspaceViewRequestSort.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceViewRequestSort.to_json())

# convert the object into a dict
create_workspace_view_request_sort_dict = create_workspace_view_request_sort_instance.to_dict()
# create an instance of CreateWorkspaceViewRequestSort from a dict
create_workspace_view_request_sort_from_dict = CreateWorkspaceViewRequestSort.from_dict(create_workspace_view_request_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


