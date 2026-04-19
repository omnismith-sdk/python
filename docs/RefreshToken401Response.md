# RefreshToken401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.refresh_token401_response import RefreshToken401Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshToken401Response from a JSON string
refresh_token401_response_instance = RefreshToken401Response.from_json(json)
# print the JSON string representation of the object
print(RefreshToken401Response.to_json())

# convert the object into a dict
refresh_token401_response_dict = refresh_token401_response_instance.to_dict()
# create an instance of RefreshToken401Response from a dict
refresh_token401_response_from_dict = RefreshToken401Response.from_dict(refresh_token401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


