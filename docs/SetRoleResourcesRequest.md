# SetRoleResourcesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[ResourceAccessInput]**](ResourceAccessInput.md) |  | 

## Example

```python
from omnismith_sdk.models.set_role_resources_request import SetRoleResourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetRoleResourcesRequest from a JSON string
set_role_resources_request_instance = SetRoleResourcesRequest.from_json(json)
# print the JSON string representation of the object
print(SetRoleResourcesRequest.to_json())

# convert the object into a dict
set_role_resources_request_dict = set_role_resources_request_instance.to_dict()
# create an instance of SetRoleResourcesRequest from a dict
set_role_resources_request_from_dict = SetRoleResourcesRequest.from_dict(set_role_resources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


