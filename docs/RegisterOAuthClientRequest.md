# RegisterOAuthClientRequest

Dynamic Client Registration request parameters (RFC 7591) for provisioning an OAuth 2.1 client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_name** | **str** | Human-readable client application name | 
**redirect_uris** | **List[str]** | Array of authorized redirection URI strings for callback verification | 
**grant_types** | **List[str]** | Authorized OAuth grant types for this client | [optional] 
**response_types** | **List[str]** | Authorized OAuth response types for this client | [optional] 
**token_endpoint_auth_method** | **str** | Client authentication method used when calling the token endpoint | [optional] 

## Example

```python
from omnismith_sdk.models.register_o_auth_client_request import RegisterOAuthClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterOAuthClientRequest from a JSON string
register_o_auth_client_request_instance = RegisterOAuthClientRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterOAuthClientRequest.to_json())

# convert the object into a dict
register_o_auth_client_request_dict = register_o_auth_client_request_instance.to_dict()
# create an instance of RegisterOAuthClientRequest from a dict
register_o_auth_client_request_from_dict = RegisterOAuthClientRequest.from_dict(register_o_auth_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


