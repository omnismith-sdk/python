# GetJwks200ResponseKeysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Key type family | [optional] 
**use** | **str** | Intended key usage | [optional] 
**alg** | **str** | Algorithm intended for use with the key | [optional] 
**kid** | **str** | Unique Key ID thumbprint | [optional] 
**n** | **str** | Base64URL-encoded RSA public modulus | [optional] 
**e** | **str** | Base64URL-encoded RSA public exponent | [optional] 

## Example

```python
from omnismith_sdk.models.get_jwks200_response_keys_inner import GetJwks200ResponseKeysInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetJwks200ResponseKeysInner from a JSON string
get_jwks200_response_keys_inner_instance = GetJwks200ResponseKeysInner.from_json(json)
# print the JSON string representation of the object
print(GetJwks200ResponseKeysInner.to_json())

# convert the object into a dict
get_jwks200_response_keys_inner_dict = get_jwks200_response_keys_inner_instance.to_dict()
# create an instance of GetJwks200ResponseKeysInner from a dict
get_jwks200_response_keys_inner_from_dict = GetJwks200ResponseKeysInner.from_dict(get_jwks200_response_keys_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


