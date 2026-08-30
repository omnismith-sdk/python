# SwitchProject200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | New project-scoped JWT access token | [optional] 
**expires_at** | **int** | Unix timestamp when the access token expires | [optional] 
**refresh_token** | **str** | New refresh token for rotating access tokens | [optional] 
**refresh_expires_at** | **int** | Unix timestamp when the refresh token expires | [optional] 

## Example

```python
from omnismith_sdk.models.switch_project200_response import SwitchProject200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchProject200Response from a JSON string
switch_project200_response_instance = SwitchProject200Response.from_json(json)
# print the JSON string representation of the object
print(SwitchProject200Response.to_json())

# convert the object into a dict
switch_project200_response_dict = switch_project200_response_instance.to_dict()
# create an instance of SwitchProject200Response from a dict
switch_project200_response_from_dict = SwitchProject200Response.from_dict(switch_project200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


