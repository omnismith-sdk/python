# AggregateEntities200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AggregateEntitiesGroup]**](AggregateEntitiesGroup.md) |  | 
**limit** | **int** | The group cap that was applied | 
**truncated** | **bool** | True when more groups exist than were returned | 

## Example

```python
from omnismith_sdk.models.aggregate_entities200_response import AggregateEntities200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateEntities200Response from a JSON string
aggregate_entities200_response_instance = AggregateEntities200Response.from_json(json)
# print the JSON string representation of the object
print(AggregateEntities200Response.to_json())

# convert the object into a dict
aggregate_entities200_response_dict = aggregate_entities200_response_instance.to_dict()
# create an instance of AggregateEntities200Response from a dict
aggregate_entities200_response_from_dict = AggregateEntities200Response.from_dict(aggregate_entities200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


