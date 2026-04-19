# GetEntityChart200ResponseSeriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **str** |  | [optional] 
**data** | [**List[GetEntityChart200ResponseSeriesInnerDataInner]**](GetEntityChart200ResponseSeriesInnerDataInner.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.get_entity_chart200_response_series_inner import GetEntityChart200ResponseSeriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityChart200ResponseSeriesInner from a JSON string
get_entity_chart200_response_series_inner_instance = GetEntityChart200ResponseSeriesInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityChart200ResponseSeriesInner.to_json())

# convert the object into a dict
get_entity_chart200_response_series_inner_dict = get_entity_chart200_response_series_inner_instance.to_dict()
# create an instance of GetEntityChart200ResponseSeriesInner from a dict
get_entity_chart200_response_series_inner_from_dict = GetEntityChart200ResponseSeriesInner.from_dict(get_entity_chart200_response_series_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


