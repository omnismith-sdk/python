# SearchEntitiesRequestGroupKeyValue

The group key value: a list item id, an entity id, a string, a number, a boolean, or an RFC 3339 timestamp. Null for the no-value group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from omnismith_sdk.models.search_entities_request_group_key_value import SearchEntitiesRequestGroupKeyValue

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntitiesRequestGroupKeyValue from a JSON string
search_entities_request_group_key_value_instance = SearchEntitiesRequestGroupKeyValue.from_json(json)
# print the JSON string representation of the object
print(SearchEntitiesRequestGroupKeyValue.to_json())

# convert the object into a dict
search_entities_request_group_key_value_dict = search_entities_request_group_key_value_instance.to_dict()
# create an instance of SearchEntitiesRequestGroupKeyValue from a dict
search_entities_request_group_key_value_from_dict = SearchEntitiesRequestGroupKeyValue.from_dict(search_entities_request_group_key_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


