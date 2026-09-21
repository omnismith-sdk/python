# AggregateEntitiesGroup

One group of records: its key (one entry per group_by field, in request order) and the reduces computed over it (one entry per aggregation, in request order).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**List[AggregateEntitiesGroupKeyInner]**](AggregateEntitiesGroupKeyInner.md) |  | 
**aggregates** | [**List[AggregateEntitiesGroupAggregatesInner]**](AggregateEntitiesGroupAggregatesInner.md) |  | 

## Example

```python
from omnismith_sdk.models.aggregate_entities_group import AggregateEntitiesGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateEntitiesGroup from a JSON string
aggregate_entities_group_instance = AggregateEntitiesGroup.from_json(json)
# print the JSON string representation of the object
print(AggregateEntitiesGroup.to_json())

# convert the object into a dict
aggregate_entities_group_dict = aggregate_entities_group_instance.to_dict()
# create an instance of AggregateEntitiesGroup from a dict
aggregate_entities_group_from_dict = AggregateEntitiesGroup.from_dict(aggregate_entities_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


