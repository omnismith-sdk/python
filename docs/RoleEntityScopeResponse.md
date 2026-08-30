# RoleEntityScopeResponse

Filter-based entity access scope defining row-level permissions for a role under a template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | Target template UUID to which this scope applies | [optional] 
**conditions** | [**List[RoleEntityScopeConditionResponse]**](RoleEntityScopeConditionResponse.md) | List of filter criteria that entities must satisfy for users with this role to access them | [optional] 

## Example

```python
from omnismith_sdk.models.role_entity_scope_response import RoleEntityScopeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleEntityScopeResponse from a JSON string
role_entity_scope_response_instance = RoleEntityScopeResponse.from_json(json)
# print the JSON string representation of the object
print(RoleEntityScopeResponse.to_json())

# convert the object into a dict
role_entity_scope_response_dict = role_entity_scope_response_instance.to_dict()
# create an instance of RoleEntityScopeResponse from a dict
role_entity_scope_response_from_dict = RoleEntityScopeResponse.from_dict(role_entity_scope_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


