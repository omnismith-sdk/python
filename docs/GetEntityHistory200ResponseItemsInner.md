# GetEntityHistory200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Mutation timestamp in ISO 8601 format | [optional] 
**attribute_id** | **UUID** | Mutated attribute UUID | [optional] 
**old_value** | **str** | Previous serialized attribute value | [optional] 
**value** | **str** | New serialized attribute value | [optional] 
**entity_id** | **UUID** | Target entity UUID | [optional] 
**author_email** | **str** | Actor email who performed the change | [optional] 

## Example

```python
from omnismith_sdk.models.get_entity_history200_response_items_inner import GetEntityHistory200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityHistory200ResponseItemsInner from a JSON string
get_entity_history200_response_items_inner_instance = GetEntityHistory200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityHistory200ResponseItemsInner.to_json())

# convert the object into a dict
get_entity_history200_response_items_inner_dict = get_entity_history200_response_items_inner_instance.to_dict()
# create an instance of GetEntityHistory200ResponseItemsInner from a dict
get_entity_history200_response_items_inner_from_dict = GetEntityHistory200ResponseItemsInner.from_dict(get_entity_history200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


