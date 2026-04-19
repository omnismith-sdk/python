# ListRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RoleResponse]**](RoleResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_roles200_response import ListRoles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListRoles200Response from a JSON string
list_roles200_response_instance = ListRoles200Response.from_json(json)
# print the JSON string representation of the object
print(ListRoles200Response.to_json())

# convert the object into a dict
list_roles200_response_dict = list_roles200_response_instance.to_dict()
# create an instance of ListRoles200Response from a dict
list_roles200_response_from_dict = ListRoles200Response.from_dict(list_roles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


