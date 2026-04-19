# RefreshToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | New JWT access token | [optional] 
**expires_at** | **int** | Access token expiration timestamp | [optional] 
**refresh_token** | **str** | New refresh token (rotation) | [optional] 
**refresh_expires_at** | **int** | Refresh token expiration timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.refresh_token200_response import RefreshToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshToken200Response from a JSON string
refresh_token200_response_instance = RefreshToken200Response.from_json(json)
# print the JSON string representation of the object
print(RefreshToken200Response.to_json())

# convert the object into a dict
refresh_token200_response_dict = refresh_token200_response_instance.to_dict()
# create an instance of RefreshToken200Response from a dict
refresh_token200_response_from_dict = RefreshToken200Response.from_dict(refresh_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


