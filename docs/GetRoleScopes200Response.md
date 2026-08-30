# GetRoleScopes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RoleEntityScopeResponse]**](RoleEntityScopeResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.get_role_scopes200_response import GetRoleScopes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleScopes200Response from a JSON string
get_role_scopes200_response_instance = GetRoleScopes200Response.from_json(json)
# print the JSON string representation of the object
print(GetRoleScopes200Response.to_json())

# convert the object into a dict
get_role_scopes200_response_dict = get_role_scopes200_response_instance.to_dict()
# create an instance of GetRoleScopes200Response from a dict
get_role_scopes200_response_from_dict = GetRoleScopes200Response.from_dict(get_role_scopes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


