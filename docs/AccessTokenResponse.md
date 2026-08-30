# AccessTokenResponse

Metadata describing an API access token (raw secret key is omitted for security)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique UUIDv7 identifier of the access token | [optional] 
**name** | **str** | Friendly human-readable label identifying the access token | [optional] 
**expires_at** | **datetime** | Expiration timestamp in ISO 8601 UTC format | [optional] 
**created_at** | **datetime** | Creation timestamp in ISO 8601 UTC format | [optional] 
**last_used_at** | **datetime** | Timestamp when this token was last used to authenticate an API request | [optional] 

## Example

```python
from omnismith_sdk.models.access_token_response import AccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenResponse from a JSON string
access_token_response_instance = AccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AccessTokenResponse.to_json())

# convert the object into a dict
access_token_response_dict = access_token_response_instance.to_dict()
# create an instance of AccessTokenResponse from a dict
access_token_response_from_dict = AccessTokenResponse.from_dict(access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


