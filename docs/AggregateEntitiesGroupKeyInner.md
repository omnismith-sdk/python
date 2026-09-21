# AggregateEntitiesGroupKeyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The group_by entry as sent | 
**value** | [**AggregateEntitiesGroupKeyInnerValue**](AggregateEntitiesGroupKeyInnerValue.md) |  | 
**custom_value** | **str** | The list item label or the referenced record&#39;s display value; null for other types | 

## Example

```python
from omnismith_sdk.models.aggregate_entities_group_key_inner import AggregateEntitiesGroupKeyInner

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateEntitiesGroupKeyInner from a JSON string
aggregate_entities_group_key_inner_instance = AggregateEntitiesGroupKeyInner.from_json(json)
# print the JSON string representation of the object
print(AggregateEntitiesGroupKeyInner.to_json())

# convert the object into a dict
aggregate_entities_group_key_inner_dict = aggregate_entities_group_key_inner_instance.to_dict()
# create an instance of AggregateEntitiesGroupKeyInner from a dict
aggregate_entities_group_key_inner_from_dict = AggregateEntitiesGroupKeyInner.from_dict(aggregate_entities_group_key_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


