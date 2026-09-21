# ResolvedAggregateBlockResponseGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**List[ResolvedAggregateBlockResponseGroupsInnerKeyInner]**](ResolvedAggregateBlockResponseGroupsInnerKeyInner.md) | The group_by fields and their values, in configured order | [optional] 
**aggregates** | [**List[ResolvedAggregateBlockResponseGroupsInnerAggregatesInner]**](ResolvedAggregateBlockResponseGroupsInnerAggregatesInner.md) | The configured reduces for this group, in configured order | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_aggregate_block_response_groups_inner import ResolvedAggregateBlockResponseGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedAggregateBlockResponseGroupsInner from a JSON string
resolved_aggregate_block_response_groups_inner_instance = ResolvedAggregateBlockResponseGroupsInner.from_json(json)
# print the JSON string representation of the object
print(ResolvedAggregateBlockResponseGroupsInner.to_json())

# convert the object into a dict
resolved_aggregate_block_response_groups_inner_dict = resolved_aggregate_block_response_groups_inner_instance.to_dict()
# create an instance of ResolvedAggregateBlockResponseGroupsInner from a dict
resolved_aggregate_block_response_groups_inner_from_dict = ResolvedAggregateBlockResponseGroupsInner.from_dict(resolved_aggregate_block_response_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


