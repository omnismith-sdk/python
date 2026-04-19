# SearchEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_search** | **str** |  | [optional] 
**filters** | [**List[ExportEntitiesRequestFiltersInner]**](ExportEntitiesRequestFiltersInner.md) |  | [optional] 

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


