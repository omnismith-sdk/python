# SearchEntitiesRequestFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Attribute UUID, attribute slug, or standard field (id, created_at, updated_at) | [optional] 
**operator** | **str** | Filter comparison operator: eq (equals), neq (not equals), gt (greater than), lt (less than), like (substring match), not-like (negative match), empty (null/empty), not-empty (has value) | [optional] 
**value** | **str** | Comparison value serialized as string (not required for empty and not-empty operators) | [optional] 

## Example

```python
from omnismith_sdk.models.search_entities_request_filters_inner import SearchEntitiesRequestFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntitiesRequestFiltersInner from a JSON string
search_entities_request_filters_inner_instance = SearchEntitiesRequestFiltersInner.from_json(json)
# print the JSON string representation of the object
print(SearchEntitiesRequestFiltersInner.to_json())

# convert the object into a dict
search_entities_request_filters_inner_dict = search_entities_request_filters_inner_instance.to_dict()
# create an instance of SearchEntitiesRequestFiltersInner from a dict
search_entities_request_filters_inner_from_dict = SearchEntitiesRequestFiltersInner.from_dict(search_entities_request_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


