# RoleResourceAccessResponse

Resource access entry for a role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | [optional] 
**resource_id** | **UUID** |  | [optional] 
**access_level** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.role_resource_access_response import RoleResourceAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResourceAccessResponse from a JSON string
role_resource_access_response_instance = RoleResourceAccessResponse.from_json(json)
# print the JSON string representation of the object
print(RoleResourceAccessResponse.to_json())

# convert the object into a dict
role_resource_access_response_dict = role_resource_access_response_instance.to_dict()
# create an instance of RoleResourceAccessResponse from a dict
role_resource_access_response_from_dict = RoleResourceAccessResponse.from_dict(role_resource_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


