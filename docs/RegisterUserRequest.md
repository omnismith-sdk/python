# RegisterUserRequest

Payload for registering a new user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address | 
**password** | **str** | User password (min 8 chars) | 

## Example

```python
from omnismith_sdk.models.register_user_request import RegisterUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterUserRequest from a JSON string
register_user_request_instance = RegisterUserRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterUserRequest.to_json())

# convert the object into a dict
register_user_request_dict = register_user_request_instance.to_dict()
# create an instance of RegisterUserRequest from a dict
register_user_request_from_dict = RegisterUserRequest.from_dict(register_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


