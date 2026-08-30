# ResolvedChartBlockResponseSeriesInnerDataPointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** | Bucket start timestamp in ISO 8601 format | [optional] 
**value** | **float** | Aggregated metric value in bucket | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_chart_block_response_series_inner_data_points_inner import ResolvedChartBlockResponseSeriesInnerDataPointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedChartBlockResponseSeriesInnerDataPointsInner from a JSON string
resolved_chart_block_response_series_inner_data_points_inner_instance = ResolvedChartBlockResponseSeriesInnerDataPointsInner.from_json(json)
# print the JSON string representation of the object
print(ResolvedChartBlockResponseSeriesInnerDataPointsInner.to_json())

# convert the object into a dict
resolved_chart_block_response_series_inner_data_points_inner_dict = resolved_chart_block_response_series_inner_data_points_inner_instance.to_dict()
# create an instance of ResolvedChartBlockResponseSeriesInnerDataPointsInner from a dict
resolved_chart_block_response_series_inner_data_points_inner_from_dict = ResolvedChartBlockResponseSeriesInnerDataPointsInner.from_dict(resolved_chart_block_response_series_inner_data_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


