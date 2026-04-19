# AssignUserToProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**role_id** | **UUID** | The Role ID to assign | 

## Example

```python
from omnismith_sdk.models.assign_user_to_project_request import AssignUserToProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignUserToProjectRequest from a JSON string
assign_user_to_project_request_instance = AssignUserToProjectRequest.from_json(json)
# print the JSON string representation of the object
print(AssignUserToProjectRequest.to_json())

# convert the object into a dict
assign_user_to_project_request_dict = assign_user_to_project_request_instance.to_dict()
# create an instance of AssignUserToProjectRequest from a dict
assign_user_to_project_request_from_dict = AssignUserToProjectRequest.from_dict(assign_user_to_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


