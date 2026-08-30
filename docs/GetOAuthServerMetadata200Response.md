# GetOAuthServerMetadata200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | Authorization server issuer URL | [optional] 
**authorization_endpoint** | **str** | Interactive user consent URL | [optional] 
**token_endpoint** | **str** | Token issuance endpoint | [optional] 
**registration_endpoint** | **str** | Dynamic client registration endpoint (RFC 7591) | [optional] 
**revocation_endpoint** | **str** | Token revocation endpoint (RFC 7009) | [optional] 
**jwks_uri** | **str** | JSON Web Key Set URL (RFC 7517) | [optional] 
**response_types_supported** | **List[str]** |  | [optional] 
**grant_types_supported** | **List[str]** |  | [optional] 
**code_challenge_methods_supported** | **List[str]** |  | [optional] 
**scopes_supported** | **List[str]** |  | [optional] 
**token_endpoint_auth_methods_supported** | **List[str]** |  | [optional] 
**service_documentation** | **str** | URL of documentation | [optional] 
**client_uri** | **str** | URL of the application homepage | [optional] 
**logo_uri** | **str** | Logo image URL for the authorization server with transparent background | [optional] 

## Example

```python
from omnismith_sdk.models.get_o_auth_server_metadata200_response import GetOAuthServerMetadata200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthServerMetadata200Response from a JSON string
get_o_auth_server_metadata200_response_instance = GetOAuthServerMetadata200Response.from_json(json)
# print the JSON string representation of the object
print(GetOAuthServerMetadata200Response.to_json())

# convert the object into a dict
get_o_auth_server_metadata200_response_dict = get_o_auth_server_metadata200_response_instance.to_dict()
# create an instance of GetOAuthServerMetadata200Response from a dict
get_o_auth_server_metadata200_response_from_dict = GetOAuthServerMetadata200Response.from_dict(get_o_auth_server_metadata200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


