# GoogleLoginRequest

Payload for Google Sign-In authentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **str** | Google ID token credential from Google Sign-In | 

## Example

```python
from omnismith_sdk.models.google_login_request import GoogleLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleLoginRequest from a JSON string
google_login_request_instance = GoogleLoginRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleLoginRequest.to_json())

# convert the object into a dict
google_login_request_dict = google_login_request_instance.to_dict()
# create an instance of GoogleLoginRequest from a dict
google_login_request_from_dict = GoogleLoginRequest.from_dict(google_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


