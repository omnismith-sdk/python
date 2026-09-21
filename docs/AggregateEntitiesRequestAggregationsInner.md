# AggregateEntitiesRequestAggregationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**var_field** | **str** | Attribute slug or UUID to reduce. Required for every op except count, which must omit it. | [optional] 

## Example

```python
from omnismith_sdk.models.aggregate_entities_request_aggregations_inner import AggregateEntitiesRequestAggregationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateEntitiesRequestAggregationsInner from a JSON string
aggregate_entities_request_aggregations_inner_instance = AggregateEntitiesRequestAggregationsInner.from_json(json)
# print the JSON string representation of the object
print(AggregateEntitiesRequestAggregationsInner.to_json())

# convert the object into a dict
aggregate_entities_request_aggregations_inner_dict = aggregate_entities_request_aggregations_inner_instance.to_dict()
# create an instance of AggregateEntitiesRequestAggregationsInner from a dict
aggregate_entities_request_aggregations_inner_from_dict = AggregateEntitiesRequestAggregationsInner.from_dict(aggregate_entities_request_aggregations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


