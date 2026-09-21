# ResolvedAggregateBlockResponse

Computed result for an aggregate block: entities matching the template and filters, grouped and reduced per group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **UUID** | Dashboard block unique identifier | [optional] 
**title** | **str** | Block header title | [optional] 
**type** | **str** | Block type discriminator | [optional] 
**limit** | **int** | Maximum number of groups returned, as configured on the block | [optional] 
**truncated** | **bool** | Whether more groups exist beyond &#x60;limit&#x60; | [optional] 
**groups** | [**List[ResolvedAggregateBlockResponseGroupsInner]**](ResolvedAggregateBlockResponseGroupsInner.md) | One row per group, in the order configured on the block | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_aggregate_block_response import ResolvedAggregateBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedAggregateBlockResponse from a JSON string
resolved_aggregate_block_response_instance = ResolvedAggregateBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ResolvedAggregateBlockResponse.to_json())

# convert the object into a dict
resolved_aggregate_block_response_dict = resolved_aggregate_block_response_instance.to_dict()
# create an instance of ResolvedAggregateBlockResponse from a dict
resolved_aggregate_block_response_from_dict = ResolvedAggregateBlockResponse.from_dict(resolved_aggregate_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


