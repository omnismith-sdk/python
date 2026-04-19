# ResolvedListBlockResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** |  | [optional] 
**attributes** | **object** |  | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_list_block_response_items_inner import ResolvedListBlockResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedListBlockResponseItemsInner from a JSON string
resolved_list_block_response_items_inner_instance = ResolvedListBlockResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(ResolvedListBlockResponseItemsInner.to_json())

# convert the object into a dict
resolved_list_block_response_items_inner_dict = resolved_list_block_response_items_inner_instance.to_dict()
# create an instance of ResolvedListBlockResponseItemsInner from a dict
resolved_list_block_response_items_inner_from_dict = ResolvedListBlockResponseItemsInner.from_dict(resolved_list_block_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


