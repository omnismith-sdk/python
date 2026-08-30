# CreateAccessTokenRequest

Payload for generating a new programmatic API access token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Friendly human-readable label to identify the token purpose | 
**expires_at** | **datetime** | Expiration timestamp in ISO 8601 UTC format (e.g. 2026-12-31T23:59:59Z) | 

## Example

```python
from omnismith_sdk.models.create_access_token_request import CreateAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessTokenRequest from a JSON string
create_access_token_request_instance = CreateAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAccessTokenRequest.to_json())

# convert the object into a dict
create_access_token_request_dict = create_access_token_request_instance.to_dict()
# create an instance of CreateAccessTokenRequest from a dict
create_access_token_request_from_dict = CreateAccessTokenRequest.from_dict(create_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


