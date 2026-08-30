# ResolvedBlockResponse

Polymorphic container for resolved dashboard block data computed from time-series telemetry and entity repositories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **UUID** | Dashboard block unique identifier | [optional] 
**title** | **str** | Block header title | [optional] 
**type** | **str** | Block type discriminator | [optional] 
**count** | **int** | Total count of entities matching template and active filter rules | [optional] 
**value** | **float** | Current aggregated metric value | [optional] 
**min** | **float** | Configured minimum gauge scale bound | [optional] 
**max** | **float** | Configured maximum gauge scale bound | [optional] 
**percentage** | **float** | Computed progress percentage within [min, max] bounds | [optional] 
**bucket_width** | **str** | Time-bucket aggregation interval applied to telemetry metrics | [optional] 
**series** | [**List[ResolvedChartBlockResponseSeriesInner]**](ResolvedChartBlockResponseSeriesInner.md) | Time-series data grouped per entity | [optional] 
**items** | [**List[ResolvedListBlockResponseItemsInner]**](ResolvedListBlockResponseItemsInner.md) | List of matching entity records with hydrated attributes | [optional] 
**total_count** | **int** | Total number of items matching filters | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_block_response import ResolvedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedBlockResponse from a JSON string
resolved_block_response_instance = ResolvedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ResolvedBlockResponse.to_json())

# convert the object into a dict
resolved_block_response_dict = resolved_block_response_instance.to_dict()
# create an instance of ResolvedBlockResponse from a dict
resolved_block_response_from_dict = ResolvedBlockResponse.from_dict(resolved_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


