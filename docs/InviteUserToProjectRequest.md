# InviteUserToProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the user to invite | 
**role_id** | **UUID** | The Role ID to assign | 

## Example

```python
from omnismith_sdk.models.invite_user_to_project_request import InviteUserToProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserToProjectRequest from a JSON string
invite_user_to_project_request_instance = InviteUserToProjectRequest.from_json(json)
# print the JSON string representation of the object
print(InviteUserToProjectRequest.to_json())

# convert the object into a dict
invite_user_to_project_request_dict = invite_user_to_project_request_instance.to_dict()
# create an instance of InviteUserToProjectRequest from a dict
invite_user_to_project_request_from_dict = InviteUserToProjectRequest.from_dict(invite_user_to_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


