# GetEntityHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GetEntityHistory200ResponseItemsInner]**](GetEntityHistory200ResponseItemsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.get_entity_history200_response import GetEntityHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityHistory200Response from a JSON string
get_entity_history200_response_instance = GetEntityHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetEntityHistory200Response.to_json())

# convert the object into a dict
get_entity_history200_response_dict = get_entity_history200_response_instance.to_dict()
# create an instance of GetEntityHistory200Response from a dict
get_entity_history200_response_from_dict = GetEntityHistory200Response.from_dict(get_entity_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


