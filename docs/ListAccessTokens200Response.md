# ListAccessTokens200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccessTokenResponse]**](AccessTokenResponse.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_access_tokens200_response import ListAccessTokens200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAccessTokens200Response from a JSON string
list_access_tokens200_response_instance = ListAccessTokens200Response.from_json(json)
# print the JSON string representation of the object
print(ListAccessTokens200Response.to_json())

# convert the object into a dict
list_access_tokens200_response_dict = list_access_tokens200_response_instance.to_dict()
# create an instance of ListAccessTokens200Response from a dict
list_access_tokens200_response_from_dict = ListAccessTokens200Response.from_dict(list_access_tokens200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


