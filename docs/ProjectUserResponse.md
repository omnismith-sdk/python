# ProjectUserResponse

User in Project details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**user_id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**role_id** | **UUID** |  | [optional] 
**role_name** | **str** | Human-readable role name | [optional] [readonly] 
**user_email** | **str** | User&#39;s email address | [optional] [readonly] 
**user_name** | **str** | User&#39;s display name | [optional] [readonly] 
**joined_at** | **datetime** |  | [optional] 
**left_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.project_user_response import ProjectUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUserResponse from a JSON string
project_user_response_instance = ProjectUserResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectUserResponse.to_json())

# convert the object into a dict
project_user_response_dict = project_user_response_instance.to_dict()
# create an instance of ProjectUserResponse from a dict
project_user_response_from_dict = ProjectUserResponse.from_dict(project_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


