# GoogleLogin200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT access token | [optional] 
**expires_at** | **int** | Access token expiration timestamp | [optional] 
**refresh_token** | **str** | Refresh token for obtaining new access tokens | [optional] 
**refresh_expires_at** | **int** | Refresh token expiration timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.google_login200_response import GoogleLogin200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleLogin200Response from a JSON string
google_login200_response_instance = GoogleLogin200Response.from_json(json)
# print the JSON string representation of the object
print(GoogleLogin200Response.to_json())

# convert the object into a dict
google_login200_response_dict = google_login200_response_instance.to_dict()
# create an instance of GoogleLogin200Response from a dict
google_login200_response_from_dict = GoogleLogin200Response.from_dict(google_login200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


