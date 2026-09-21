# SearchEntitiesRequest

Filter and global search criteria for querying template entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_search** | **str** | Full-text query string searched across all string and text dimension attributes of the template | [optional] 
**filter_groups** | **List[List[EntityFilter]]** | Filter groups: clauses inside a group are AND-ed, groups are OR-ed. &#x60;[]&#x60; applies no filter, &#x60;[[a, b]]&#x60; is &#x60;a AND b&#x60;, &#x60;[[a], [b, c]]&#x60; is &#x60;a OR (b AND c)&#x60;. | [optional] 
**verbose** | **bool** | When true, each record&#39;s attribute_values is an array of EntityAttributeValue items (attribute id, slug, raw value, resolved custom_value, reference_entity_id). When false (default), attribute_values is a compact object mapping attribute slug to display value, with the ids behind list, reference and file labels in list_item_ids, reference_entity_ids and file_ids. | [optional] [default to False]
**fields** | **List[str]** | Optional list of attribute slugs, attribute UUIDs, or root fields to project (e.g. [\&quot;title\&quot;, \&quot;status\&quot;]). When specified, database queries only hydrate the requested attributes, drastically reducing response payload size and execution latency. If omitted, all attributes defined on the template are returned. | [optional] 

## Example

```python
from omnismith_sdk.models.search_entities_request import SearchEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntitiesRequest from a JSON string
search_entities_request_instance = SearchEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(SearchEntitiesRequest.to_json())

# convert the object into a dict
search_entities_request_dict = search_entities_request_instance.to_dict()
# create an instance of SearchEntitiesRequest from a dict
search_entities_request_from_dict = SearchEntitiesRequest.from_dict(search_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


