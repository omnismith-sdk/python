# ResolvedChartBlockResponseSeriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**data_points** | [**List[GetEntityChart200ResponseSeriesInnerDataInner]**](GetEntityChart200ResponseSeriesInnerDataInner.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_chart_block_response_series_inner import ResolvedChartBlockResponseSeriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedChartBlockResponseSeriesInner from a JSON string
resolved_chart_block_response_series_inner_instance = ResolvedChartBlockResponseSeriesInner.from_json(json)
# print the JSON string representation of the object
print(ResolvedChartBlockResponseSeriesInner.to_json())

# convert the object into a dict
resolved_chart_block_response_series_inner_dict = resolved_chart_block_response_series_inner_instance.to_dict()
# create an instance of ResolvedChartBlockResponseSeriesInner from a dict
resolved_chart_block_response_series_inner_from_dict = ResolvedChartBlockResponseSeriesInner.from_dict(resolved_chart_block_response_series_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


