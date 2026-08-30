# RevokeOAuthTokenRequest

OAuth 2.0 token revocation request (RFC 7009) to invalidate active refresh or access tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token string that the client wants to revoke | 
**token_type_hint** | **str** | Hint about the type of token submitted for revocation | [optional] 
**client_id** | **str** | Client identifier | [optional] 

## Example

```python
from omnismith_sdk.models.revoke_o_auth_token_request import RevokeOAuthTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeOAuthTokenRequest from a JSON string
revoke_o_auth_token_request_instance = RevokeOAuthTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeOAuthTokenRequest.to_json())

# convert the object into a dict
revoke_o_auth_token_request_dict = revoke_o_auth_token_request_instance.to_dict()
# create an instance of RevokeOAuthTokenRequest from a dict
revoke_o_auth_token_request_from_dict = RevokeOAuthTokenRequest.from_dict(revoke_o_auth_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


