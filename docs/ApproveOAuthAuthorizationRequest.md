# ApproveOAuthAuthorizationRequest

Submits user consent approval for an authorized OAuth client and the set of projects it may reach.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client identifier | 
**redirect_uri** | **str** | Redirection URI to return the authorization code | 
**project_ids** | **List[UUID]** | Every project UUID the client is granted. The first is the project the credential acts on until it selects another, and the set bounds what it can ever reach. There is no wildcard: a grant names its projects explicitly, so it cannot silently widen as the user creates more. | 
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


