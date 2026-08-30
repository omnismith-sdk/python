# ApproveOAuthAuthorization200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Single-use authorization code | [optional] 
**redirect_uri** | **str** | Client redirection URI | [optional] 
**callback_url** | **str** | Complete redirection callback URL with code and state parameters | [optional] 
**state** | **str** | Echoed client state parameter | [optional] 

## Example

```python
from omnismith_sdk.models.approve_o_auth_authorization200_response import ApproveOAuthAuthorization200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveOAuthAuthorization200Response from a JSON string
approve_o_auth_authorization200_response_instance = ApproveOAuthAuthorization200Response.from_json(json)
# print the JSON string representation of the object
print(ApproveOAuthAuthorization200Response.to_json())

# convert the object into a dict
approve_o_auth_authorization200_response_dict = approve_o_auth_authorization200_response_instance.to_dict()
# create an instance of ApproveOAuthAuthorization200Response from a dict
approve_o_auth_authorization200_response_from_dict = ApproveOAuthAuthorization200Response.from_dict(approve_o_auth_authorization200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


