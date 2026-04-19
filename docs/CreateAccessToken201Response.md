# CreateAccessToken201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**api_key** | **str** | The raw API key. Shown once only. | [optional] 
**expires_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

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


