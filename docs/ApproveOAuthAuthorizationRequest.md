# ApproveOAuthAuthorizationRequest

Submits user consent approval for an authorized OAuth client and selected project workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client identifier | 
**redirect_uri** | **str** | Redirection URI to return the authorization code | 
**project_id** | **str** | Selected Project UUID that client will be authorized to access | 
**code_challenge** | **str** | PKCE code challenge string (RFC 7636) | 
**code_challenge_method** | **str** | PKCE challenge transformation method | [optional] 
**scopes** | **List[str]** | Authorized scope strings | [optional] 
**state** | **str** | Opaque client state parameter for CSRF mitigation | [optional] 

## Example

```python
from omnismith_sdk.models.approve_o_auth_authorization_request import ApproveOAuthAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveOAuthAuthorizationRequest from a JSON string
approve_o_auth_authorization_request_instance = ApproveOAuthAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveOAuthAuthorizationRequest.to_json())

# convert the object into a dict
approve_o_auth_authorization_request_dict = approve_o_auth_authorization_request_instance.to_dict()
# create an instance of ApproveOAuthAuthorizationRequest from a dict
approve_o_auth_authorization_request_from_dict = ApproveOAuthAuthorizationRequest.from_dict(approve_o_auth_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


