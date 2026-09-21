# AggregateEntitiesGroupAggregatesInnerValue

count: integer. sum/avg/min/max on numbers: float. min/max on dates: RFC 3339 string. Null when no record in the group has a value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from omnismith_sdk.models.aggregate_entities_group_aggregates_inner_value import AggregateEntitiesGroupAggregatesInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateEntitiesGroupAggregatesInnerValue from a JSON string
aggregate_entities_group_aggregates_inner_value_instance = AggregateEntitiesGroupAggregatesInnerValue.from_json(json)
# print the JSON string representation of the object
print(AggregateEntitiesGroupAggregatesInnerValue.to_json())

# convert the object into a dict
aggregate_entities_group_aggregates_inner_value_dict = aggregate_entities_group_aggregates_inner_value_instance.to_dict()
# create an instance of AggregateEntitiesGroupAggregatesInnerValue from a dict
aggregate_entities_group_aggregates_inner_value_from_dict = AggregateEntitiesGroupAggregatesInnerValue.from_dict(aggregate_entities_group_aggregates_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


