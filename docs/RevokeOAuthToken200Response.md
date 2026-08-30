# RevokeOAuthToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoked** | **bool** | Whether the token is no longer active | [optional] 

## Example

```python
from omnismith_sdk.models.revoke_o_auth_token200_response import RevokeOAuthToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeOAuthToken200Response from a JSON string
revoke_o_auth_token200_response_instance = RevokeOAuthToken200Response.from_json(json)
# print the JSON string representation of the object
print(RevokeOAuthToken200Response.to_json())

# convert the object into a dict
revoke_o_auth_token200_response_dict = revoke_o_auth_token200_response_instance.to_dict()
# create an instance of RevokeOAuthToken200Response from a dict
revoke_o_auth_token200_response_from_dict = RevokeOAuthToken200Response.from_dict(revoke_o_auth_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


