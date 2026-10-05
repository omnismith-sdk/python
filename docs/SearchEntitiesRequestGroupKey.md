# SearchEntitiesRequestGroupKey

Narrows the result to one group reported by aggregate_entities: pass the `field` and `value` of a group key back unchanged. `value` null selects the records that have no value for the field. Omit the property to search all records. Combines with filter_groups, global_search and sorting; the total then equals the group's count. The field must be groupable (list, reference, string, number, boolean, date or datetime) and the value must have the type aggregate_entities reports for it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Attribute slug or UUID | 
**value** | [**SearchEntitiesRequestGroupKeyValue**](SearchEntitiesRequestGroupKeyValue.md) |  | 

## Example

```python
from omnismith_sdk.models.search_entities_request_group_key import SearchEntitiesRequestGroupKey

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntitiesRequestGroupKey from a JSON string
search_entities_request_group_key_instance = SearchEntitiesRequestGroupKey.from_json(json)
# print the JSON string representation of the object
print(SearchEntitiesRequestGroupKey.to_json())

# convert the object into a dict
search_entities_request_group_key_dict = search_entities_request_group_key_instance.to_dict()
# create an instance of SearchEntitiesRequestGroupKey from a dict
search_entities_request_group_key_from_dict = SearchEntitiesRequestGroupKey.from_dict(search_entities_request_group_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


