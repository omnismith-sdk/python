# RegisterOAuthClient201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Generated unique client identifier | [optional] 
**client_secret** | **str** | Client secret for confidential clients (null for public clients) | [optional] 
**client_name** | **str** | Registered application name | [optional] 
**redirect_uris** | **List[str]** | Authorized redirection URIs | [optional] 
**grant_types** | **List[str]** | Permitted grant types | [optional] 
**response_types** | **List[str]** | Permitted response types | [optional] 
**token_endpoint_auth_method** | **str** | Authentication method required at token endpoint | [optional] 
**client_id_issued_at** | **int** | Unix timestamp when client was registered | [optional] 

## Example

```python
from omnismith_sdk.models.register_o_auth_client201_response import RegisterOAuthClient201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterOAuthClient201Response from a JSON string
register_o_auth_client201_response_instance = RegisterOAuthClient201Response.from_json(json)
# print the JSON string representation of the object
print(RegisterOAuthClient201Response.to_json())

# convert the object into a dict
register_o_auth_client201_response_dict = register_o_auth_client201_response_instance.to_dict()
# create an instance of RegisterOAuthClient201Response from a dict
register_o_auth_client201_response_from_dict = RegisterOAuthClient201Response.from_dict(register_o_auth_client201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


