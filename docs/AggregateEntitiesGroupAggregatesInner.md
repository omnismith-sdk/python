# AggregateEntitiesGroupAggregatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**var_field** | **str** | The aggregation field as sent; null for count | 
**value** | [**AggregateEntitiesGroupAggregatesInnerValue**](AggregateEntitiesGroupAggregatesInnerValue.md) |  | 

## Example

```python
from omnismith_sdk.models.aggregate_entities_group_aggregates_inner import AggregateEntitiesGroupAggregatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateEntitiesGroupAggregatesInner from a JSON string
aggregate_entities_group_aggregates_inner_instance = AggregateEntitiesGroupAggregatesInner.from_json(json)
# print the JSON string representation of the object
print(AggregateEntitiesGroupAggregatesInner.to_json())

# convert the object into a dict
aggregate_entities_group_aggregates_inner_dict = aggregate_entities_group_aggregates_inner_instance.to_dict()
# create an instance of AggregateEntitiesGroupAggregatesInner from a dict
aggregate_entities_group_aggregates_inner_from_dict = AggregateEntitiesGroupAggregatesInner.from_dict(aggregate_entities_group_aggregates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


