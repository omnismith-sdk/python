# DuplicateWorkspaceRequest

Payload for duplicating an existing workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str** | Custom name for the duplicated workspace; if omitted, defaults to the source name with a (Copy) suffix | [optional] 

## Example

```python
from omnismith_sdk.models.duplicate_workspace_request import DuplicateWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateWorkspaceRequest from a JSON string
duplicate_workspace_request_instance = DuplicateWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(DuplicateWorkspaceRequest.to_json())

# convert the object into a dict
duplicate_workspace_request_dict = duplicate_workspace_request_instance.to_dict()
# create an instance of DuplicateWorkspaceRequest from a dict
duplicate_workspace_request_from_dict = DuplicateWorkspaceRequest.from_dict(duplicate_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


