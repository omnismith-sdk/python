# OAuthTokenRequest

OAuth 2.0 token grant request (RFC 6749 / RFC 7636) for authorization_code or refresh_token grant types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | OAuth 2.0 grant type | 
**client_id** | **str** | OAuth client identifier | [optional] 
**client_secret** | **str** | OAuth client secret (for confidential clients) | [optional] 
**code** | **str** | Authorization code obtained from /oauth/authorize/approve | [optional] 
**redirect_uri** | **str** | Original redirection URI matching the authorization request | [optional] 
**code_verifier** | **str** | PKCE code verifier (RFC 7636) | [optional] 
**refresh_token** | **str** | Refresh token for grant_type&#x3D;refresh_token | [optional] 
**scope** | **str** | Requested scope | [optional] 

## Example

```python
from omnismith_sdk.models.o_auth_token_request import OAuthTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthTokenRequest from a JSON string
o_auth_token_request_instance = OAuthTokenRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthTokenRequest.to_json())

# convert the object into a dict
o_auth_token_request_dict = o_auth_token_request_instance.to_dict()
# create an instance of OAuthTokenRequest from a dict
o_auth_token_request_from_dict = OAuthTokenRequest.from_dict(o_auth_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


