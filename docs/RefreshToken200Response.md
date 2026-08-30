# RefreshToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | New JWT access token for authenticating Bearer requests | [optional] 
**expires_at** | **int** | Unix timestamp when the access token expires | [optional] 
**refresh_token** | **str** | New rotated refresh token for future refreshes | [optional] 
**refresh_expires_at** | **int** | Unix timestamp when the new refresh token expires | [optional] 

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


