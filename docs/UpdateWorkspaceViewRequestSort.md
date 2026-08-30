# UpdateWorkspaceViewRequestSort

Updated sort configuration defining target attribute and direction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **str** | Attribute key or column to sort by | [optional] 
**direction** | **str** | Sort direction | [optional] 

## Example

```python
from omnismith_sdk.models.update_workspace_view_request_sort import UpdateWorkspaceViewRequestSort

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceViewRequestSort from a JSON string
update_workspace_view_request_sort_instance = UpdateWorkspaceViewRequestSort.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkspaceViewRequestSort.to_json())

# convert the object into a dict
update_workspace_view_request_sort_dict = update_workspace_view_request_sort_instance.to_dict()
# create an instance of UpdateWorkspaceViewRequestSort from a dict
update_workspace_view_request_sort_from_dict = UpdateWorkspaceViewRequestSort.from_dict(update_workspace_view_request_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


