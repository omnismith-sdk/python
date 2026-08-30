# RoleEntityScopeConditionResponse

Individual attribute filter condition for row-level access control

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Attribute UUID or standard entity field (e.g. id, created_at) | [optional] 
**operator** | **str** | Comparison operator | [optional] 
**value** | **str** | Comparison value | [optional] 

## Example

```python
from omnismith_sdk.models.role_entity_scope_condition_response import RoleEntityScopeConditionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleEntityScopeConditionResponse from a JSON string
role_entity_scope_condition_response_instance = RoleEntityScopeConditionResponse.from_json(json)
# print the JSON string representation of the object
print(RoleEntityScopeConditionResponse.to_json())

# convert the object into a dict
role_entity_scope_condition_response_dict = role_entity_scope_condition_response_instance.to_dict()
# create an instance of RoleEntityScopeConditionResponse from a dict
role_entity_scope_condition_response_from_dict = RoleEntityScopeConditionResponse.from_dict(role_entity_scope_condition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


