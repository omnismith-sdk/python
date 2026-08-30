# GetOAuthAuthorizeInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | OAuth client identifier | [optional] 
**client_name** | **str** | Human-readable client application name | [optional] 
**redirect_uri** | **str** | Validated redirection callback URI | [optional] 
**scopes** | **List[str]** | List of requested scopes | [optional] 
**user_email** | **str** | Email address of the currently authenticated user | [optional] 
**active_project_id** | **str** | Currently active project ID for the user session | [optional] 
**projects** | [**List[GetOAuthAuthorizeInfo200ResponseProjectsInner]**](GetOAuthAuthorizeInfo200ResponseProjectsInner.md) | List of projects accessible by the authenticated user | [optional] 
**state** | **str** | Echoed client state parameter | [optional] 

## Example

```python
from omnismith_sdk.models.get_o_auth_authorize_info200_response import GetOAuthAuthorizeInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthAuthorizeInfo200Response from a JSON string
get_o_auth_authorize_info200_response_instance = GetOAuthAuthorizeInfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetOAuthAuthorizeInfo200Response.to_json())

# convert the object into a dict
get_o_auth_authorize_info200_response_dict = get_o_auth_authorize_info200_response_instance.to_dict()
# create an instance of GetOAuthAuthorizeInfo200Response from a dict
get_o_auth_authorize_info200_response_from_dict = GetOAuthAuthorizeInfo200Response.from_dict(get_o_auth_authorize_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


