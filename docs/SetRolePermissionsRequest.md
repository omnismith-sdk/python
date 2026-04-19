# SetRolePermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | 

## Example

```python
from omnismith_sdk.models.set_role_permissions_request import SetRolePermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetRolePermissionsRequest from a JSON string
set_role_permissions_request_instance = SetRolePermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(SetRolePermissionsRequest.to_json())

# convert the object into a dict
set_role_permissions_request_dict = set_role_permissions_request_instance.to_dict()
# create an instance of SetRolePermissionsRequest from a dict
set_role_permissions_request_from_dict = SetRolePermissionsRequest.from_dict(set_role_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


