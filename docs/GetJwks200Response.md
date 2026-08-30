# GetJwks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[GetJwks200ResponseKeysInner]**](GetJwks200ResponseKeysInner.md) | Array of public cryptographic key descriptors | [optional] 

## Example

```python
from omnismith_sdk.models.get_jwks200_response import GetJwks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetJwks200Response from a JSON string
get_jwks200_response_instance = GetJwks200Response.from_json(json)
# print the JSON string representation of the object
print(GetJwks200Response.to_json())

# convert the object into a dict
get_jwks200_response_dict = get_jwks200_response_instance.to_dict()
# create an instance of GetJwks200Response from a dict
get_jwks200_response_from_dict = GetJwks200Response.from_dict(get_jwks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


