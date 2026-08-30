# SessionResponse

Detailed metadata describing a user login session and token status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique UUID identifier of the session | [optional] 
**user_id** | **UUID** | UUID of the authenticated user | [optional] 
**email** | **str** | Email address of the session owner | [optional] 
**role_id** | **UUID** | Active role UUID under this session | [optional] 
**ip_address** | **str** | Client IP address from which the session was established | [optional] 
**user_agent** | **str** | User-Agent header string of the client browser/application | [optional] 
**created_at** | **datetime** | Timestamp when the session was created | [optional] 
**expires_at** | **datetime** | Expiration timestamp after which the session becomes invalid | [optional] 
**revoked_at** | **datetime** | Timestamp when the session was explicitly revoked | [optional] 
**revoked_by** | **UUID** | User UUID who revoked the session | [optional] 
**revoked_reason** | **str** | Reason note provided upon session revocation | [optional] 
**status** | **str** | Current session status state | [optional] 

## Example

```python
from omnismith_sdk.models.session_response import SessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionResponse from a JSON string
session_response_instance = SessionResponse.from_json(json)
# print the JSON string representation of the object
print(SessionResponse.to_json())

# convert the object into a dict
session_response_dict = session_response_instance.to_dict()
# create an instance of SessionResponse from a dict
session_response_from_dict = SessionResponse.from_dict(session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


