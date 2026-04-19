# GetEntityChart200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[GetEntityChart200ResponseSeriesInner]**](GetEntityChart200ResponseSeriesInner.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.get_entity_chart200_response import GetEntityChart200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityChart200Response from a JSON string
get_entity_chart200_response_instance = GetEntityChart200Response.from_json(json)
# print the JSON string representation of the object
print(GetEntityChart200Response.to_json())

# convert the object into a dict
get_entity_chart200_response_dict = get_entity_chart200_response_instance.to_dict()
# create an instance of GetEntityChart200Response from a dict
get_entity_chart200_response_from_dict = GetEntityChart200Response.from_dict(get_entity_chart200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


