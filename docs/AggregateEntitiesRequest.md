# AggregateEntitiesRequest

Which records to reduce, how to group them, and which reduces to compute per group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_groups** | **List[List[EntityFilter]]** | Narrows the records before grouping. Same grammar as the search endpoint: Filter groups: clauses inside a group are AND-ed, groups are OR-ed. &#x60;[]&#x60; applies no filter, &#x60;[[a, b]]&#x60; is &#x60;a AND b&#x60;, &#x60;[[a], [b, c]]&#x60; is &#x60;a OR (b AND c)&#x60;. | [optional] 
**group_by** | **List[str]** | Attribute slugs or UUIDs to group by, at most 3. Lists, references, strings, numbers, booleans and dates can be keys; metrics, markdown, files and images cannot. Empty groups the whole filtered set into one row. | [optional] 
**aggregations** | [**List[AggregateEntitiesRequestAggregationsInner]**](AggregateEntitiesRequestAggregationsInner.md) | Reduces computed for every group, reported back in this order. &#x60;count&#x60; takes no field; &#x60;sum&#x60; and &#x60;avg&#x60; need a number attribute; &#x60;min&#x60; and &#x60;max&#x60; accept number, date and datetime attributes. | 
**limit** | **int** | Maximum number of groups returned (1-100). The response says whether more groups exist. | [optional] [default to 50]

## Example

```python
from omnismith_sdk.models.aggregate_entities_request import AggregateEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateEntitiesRequest from a JSON string
aggregate_entities_request_instance = AggregateEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(AggregateEntitiesRequest.to_json())

# convert the object into a dict
aggregate_entities_request_dict = aggregate_entities_request_instance.to_dict()
# create an instance of AggregateEntitiesRequest from a dict
aggregate_entities_request_from_dict = AggregateEntitiesRequest.from_dict(aggregate_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


