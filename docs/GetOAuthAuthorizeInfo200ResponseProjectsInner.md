# GetOAuthAuthorizeInfo200ResponseProjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Project UUID | [optional] 
**name** | **str** | Project display name | [optional] 
**is_owner** | **bool** | Whether the user is the project owner | [optional] 
**role_name** | **str** | User role within the project | [optional] 

## Example

```python
from omnismith_sdk.models.get_o_auth_authorize_info200_response_projects_inner import GetOAuthAuthorizeInfo200ResponseProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthAuthorizeInfo200ResponseProjectsInner from a JSON string
get_o_auth_authorize_info200_response_projects_inner_instance = GetOAuthAuthorizeInfo200ResponseProjectsInner.from_json(json)
# print the JSON string representation of the object
print(GetOAuthAuthorizeInfo200ResponseProjectsInner.to_json())

# convert the object into a dict
get_o_auth_authorize_info200_response_projects_inner_dict = get_o_auth_authorize_info200_response_projects_inner_instance.to_dict()
# create an instance of GetOAuthAuthorizeInfo200ResponseProjectsInner from a dict
get_o_auth_authorize_info200_response_projects_inner_from_dict = GetOAuthAuthorizeInfo200ResponseProjectsInner.from_dict(get_o_auth_authorize_info200_response_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


