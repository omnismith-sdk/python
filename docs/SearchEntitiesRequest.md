# SearchEntitiesRequest

Filter and global search criteria for querying template entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_search** | **str** | Full-text query string searched across all string and text dimension attributes of the template | [optional] 
**filters** | [**List[SearchEntitiesRequestFiltersInner]**](SearchEntitiesRequestFiltersInner.md) | List of structured attribute and metadata filter conditions | [optional] 
**attribute_key** | **str** | Format for attribute_values dictionary keys: \&quot;id\&quot; for UUIDs or \&quot;slug\&quot; for attribute slugs | [optional] 

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


