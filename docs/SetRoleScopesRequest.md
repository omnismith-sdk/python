# SetRoleScopesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | [**List[ScopeAccessInput]**](ScopeAccessInput.md) |  | 

## Example

```python
from omnismith_sdk.models.set_role_scopes_request import SetRoleScopesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetRoleScopesRequest from a JSON string
set_role_scopes_request_instance = SetRoleScopesRequest.from_json(json)
# print the JSON string representation of the object
print(SetRoleScopesRequest.to_json())

# convert the object into a dict
set_role_scopes_request_dict = set_role_scopes_request_instance.to_dict()
# create an instance of SetRoleScopesRequest from a dict
set_role_scopes_request_from_dict = SetRoleScopesRequest.from_dict(set_role_scopes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


