# ResolvedChartBlockResponse

Computed result for a time-series telemetry chart block aggregated across query intervals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **UUID** | Dashboard block unique identifier | [optional] 
**title** | **str** | Block header title | [optional] 
**type** | **str** | Block type discriminator | [optional] 
**bucket_width** | **str** | Time-bucket aggregation interval applied to telemetry metrics | [optional] 
**series** | [**List[ResolvedChartBlockResponseSeriesInner]**](ResolvedChartBlockResponseSeriesInner.md) | Time-series data grouped per entity | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_chart_block_response import ResolvedChartBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedChartBlockResponse from a JSON string
resolved_chart_block_response_instance = ResolvedChartBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ResolvedChartBlockResponse.to_json())

# convert the object into a dict
resolved_chart_block_response_dict = resolved_chart_block_response_instance.to_dict()
# create an instance of ResolvedChartBlockResponse from a dict
resolved_chart_block_response_from_dict = ResolvedChartBlockResponse.from_dict(resolved_chart_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


