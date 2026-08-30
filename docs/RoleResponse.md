# RoleResponse

Metadata describing a system or custom user role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique UUIDv7 identifier of the role | [optional] 
**name** | **str** | Display name of the role | [optional] 
**is_owner** | **bool** | Whether this is the root project owner role with full administrative privileges | [optional] 
**created_at** | **datetime** | Timestamp when the role was created | [optional] 

## Example

```python
from omnismith_sdk.models.role_response import RoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResponse from a JSON string
role_response_instance = RoleResponse.from_json(json)
# print the JSON string representation of the object
print(RoleResponse.to_json())

# convert the object into a dict
role_response_dict = role_response_instance.to_dict()
# create an instance of RoleResponse from a dict
role_response_from_dict = RoleResponse.from_dict(role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


