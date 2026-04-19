# ResolvedBlockResponse

Resolved block data with computed values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **UUID** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**value** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**bucket_width** | **str** |  | [optional] 
**series** | [**List[ResolvedChartBlockResponseSeriesInner]**](ResolvedChartBlockResponseSeriesInner.md) |  | [optional] 
**items** | [**List[ResolvedListBlockResponseItemsInner]**](ResolvedListBlockResponseItemsInner.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

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


