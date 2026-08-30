# ExchangeOAuthToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | RS256 JWT access token | [optional] 
**token_type** | **str** | Token type (Bearer) | [optional] 
**expires_in** | **int** | Access token lifetime in seconds | [optional] 
**refresh_token** | **str** | Rotating refresh token for renewing credentials | [optional] 
**scope** | **str** | Granted scope strings | [optional] 

## Example

```python
from omnismith_sdk.models.exchange_o_auth_token200_response import ExchangeOAuthToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeOAuthToken200Response from a JSON string
exchange_o_auth_token200_response_instance = ExchangeOAuthToken200Response.from_json(json)
# print the JSON string representation of the object
print(ExchangeOAuthToken200Response.to_json())

# convert the object into a dict
exchange_o_auth_token200_response_dict = exchange_o_auth_token200_response_instance.to_dict()
# create an instance of ExchangeOAuthToken200Response from a dict
exchange_o_auth_token200_response_from_dict = ExchangeOAuthToken200Response.from_dict(exchange_o_auth_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


