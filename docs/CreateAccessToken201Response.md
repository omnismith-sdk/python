# CreateAccessToken201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique UUIDv7 identifier of the created access token | [optional] 
**name** | **str** | Friendly human-readable label assigned to the access token | [optional] 
**api_key** | **str** | The raw secret API key starting with &#x60;omni_&#x60;. Displayed once only upon creation. | [optional] 
**expires_at** | **datetime** | Expiration timestamp in ISO 8601 UTC format | [optional] 
**created_at** | **datetime** | Creation timestamp in ISO 8601 UTC format | [optional] 

## Example

```python
from omnismith_sdk.models.create_access_token201_response import CreateAccessToken201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessToken201Response from a JSON string
create_access_token201_response_instance = CreateAccessToken201Response.from_json(json)
# print the JSON string representation of the object
print(CreateAccessToken201Response.to_json())

# convert the object into a dict
create_access_token201_response_dict = create_access_token201_response_instance.to_dict()
# create an instance of CreateAccessToken201Response from a dict
create_access_token201_response_from_dict = CreateAccessToken201Response.from_dict(create_access_token201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


