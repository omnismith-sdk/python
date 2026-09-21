# AggregateEntitiesGroupKeyInnerValue

The stored value: a list item id, an entity id, a string, a number, a boolean, or an RFC 3339 date. Null groups the records that have no value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from omnismith_sdk.models.aggregate_entities_group_key_inner_value import AggregateEntitiesGroupKeyInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateEntitiesGroupKeyInnerValue from a JSON string
aggregate_entities_group_key_inner_value_instance = AggregateEntitiesGroupKeyInnerValue.from_json(json)
# print the JSON string representation of the object
print(AggregateEntitiesGroupKeyInnerValue.to_json())

# convert the object into a dict
aggregate_entities_group_key_inner_value_dict = aggregate_entities_group_key_inner_value_instance.to_dict()
# create an instance of AggregateEntitiesGroupKeyInnerValue from a dict
aggregate_entities_group_key_inner_value_from_dict = AggregateEntitiesGroupKeyInnerValue.from_dict(aggregate_entities_group_key_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


