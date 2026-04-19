# GetEntityHistory200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**author_email** | **str** |  | [optional] 

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


