# GetAllTiers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TierResponse]**](TierResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.get_all_tiers200_response import GetAllTiers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllTiers200Response from a JSON string
get_all_tiers200_response_instance = GetAllTiers200Response.from_json(json)
# print the JSON string representation of the object
print(GetAllTiers200Response.to_json())

# convert the object into a dict
get_all_tiers200_response_dict = get_all_tiers200_response_instance.to_dict()
# create an instance of GetAllTiers200Response from a dict
get_all_tiers200_response_from_dict = GetAllTiers200Response.from_dict(get_all_tiers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


